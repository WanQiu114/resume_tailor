"""Copy immutable templates, compile application copies, and produce PDF evidence."""
import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(folder):
    files = sorted(folder.rglob('*'))
    if any(p.is_symlink() or p.is_junction() for p in files if hasattr(p, 'is_junction')):
        raise ValueError('Template links are not supported; use regular files.')
    if any(p.is_symlink() for p in files):
        raise ValueError('Template symlinks are not supported.')
    return {str(p.relative_to(folder)): digest(p) for p in files if p.is_file()}


def safe_part(value):
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '', value)
    value = re.sub(r'\s+', '_', value.strip()).strip(' ._')
    if not value or value in {'.', '..'}:
        raise ValueError('Company and job title must contain filename-safe text.')
    return value[:64]


def paired(folder, name, record):
    """Markdown includes every JSON field; structured JSONL is canonical."""
    folder.mkdir(parents=True, exist_ok=True)
    record['updated_at'] = datetime.now(timezone.utc).isoformat()
    (folder / (name + '.jsonl')).write_text(json.dumps(record, ensure_ascii=False) + '\n', encoding='utf-8')
    chunks = ['# ' + name.replace('_', ' ').title(), '']
    for key, value in record.items():
        chunks += ['## ' + key, '']
        if key == 'unified_diff':
            chunks += ['```diff', value, '```', '']
        elif isinstance(value, (dict, list)):
            chunks += ['```json', json.dumps(value, ensure_ascii=False, indent=2), '```', '']
        else:
            chunks += [str(value), '']
    (folder / (name + '.md')).write_text('\n'.join(chunks), encoding='utf-8')


def prepare(root, kind, company, title):
    template = root / 'template'
    selected = ('CV' if kind == 'CV' else 'resume') + '_template.tex'
    for name in (selected, 'resume.cls'):
        if not (template / name).is_file():
            raise FileNotFoundError(template / name)
    hashes = snapshot(template)
    base = f'HeYang_Yuan_{kind}_{safe_part(company)}_{safe_part(title)}'
    stem, number = base, 2
    while any((root / path).exists() for path in (
        f'resumes/latex/{stem}.tex', f'resumes/pdfs/{stem}.pdf', f'resumes/reviews/{stem}')):
        stem = f'{base}_{number:02d}'
        number += 1
    source = root / 'resumes/latex' / (stem + '.tex')
    deps = source.parent / 'dependencies' / stem
    deps.mkdir(parents=True)
    for name in hashes:
        if name in ('CV_template.tex', 'resume_template.tex'):
            continue
        target = deps / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(template / name, target)
    shutil.copy2(template / selected, source)
    if snapshot(template) != hashes:
        raise RuntimeError('Template changed during preparation.')
    record = dict(schema_version=1, task_id=stem, company=company, job_title=title,
                  kind=kind, template=selected, template_hashes=hashes,
                  source=str(source.relative_to(root)), dependencies=str(deps.relative_to(root)),
                  initial_source_sha256=digest(source), status='prepared',
                  assumptions=[], unresolved_issues=['JD analysis and tailoring not yet performed.'])
    folder = root / 'resumes/reviews' / stem
    paired(folder, 'manifest', record)
    shutil.copy2(source, folder / 'initial.tex')
    return record


def engine_path(root, override):
    if override:
        path = shutil.which(override) or (override if Path(override).is_file() else None)
        if not path:
            raise FileNotFoundError('Requested LaTeX engine not found: ' + override)
        return str(Path(path).resolve())
    local = root / 'tools/tectonic/tectonic.exe'
    if local.is_file():
        return str(local)
    for name in ('tectonic', 'xelatex', 'pdflatex', 'lualatex'):
        if shutil.which(name):
            return shutil.which(name)
    raise RuntimeError('No LaTeX engine. Configure tools/tectonic/tectonic.exe or install a TeX engine.')


def build(root, stem, override=None):
    if Path(stem).name != stem or '/' in stem or '\\' in stem or stem in ('.', '..'):
        raise ValueError('Use a bare application stem, not a path.')
    folder = root / 'resumes/reviews' / stem
    manifest = json.loads((folder / 'manifest.jsonl').read_text(encoding='utf-8'))
    source = root / manifest['source']
    # Manifest paths must stay in this application's generated area.
    if source.resolve() != (root / 'resumes/latex' / (stem + '.tex')).resolve():
        raise ValueError('Invalid manifest source path.')
    deps = root / 'resumes/latex/dependencies' / stem
    hashes = snapshot(root / 'template')
    record = dict(schema_version=1, task_id=stem, kind=manifest['kind'],
                  source_sha256=digest(source), template_unchanged_since_prepare=(hashes == manifest['template_hashes']),
                  status='failed', compile_status='not_run', visual_status='pending',
                  reading_order_status='pending', ats_status='not_certified', warnings=[])
    try:
        if hashes != manifest['template_hashes']:
            raise RuntimeError('Template differs from preparation snapshot. Review the change before continuing.')
        compiler = engine_path(root, override)
        # A new build directory prevents a failed compilation from publishing a stale PDF.
        import tempfile
        parent = root / 'resumes/build'
        parent.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix='run-', dir=parent))
        shutil.copytree(deps, stage, dirs_exist_ok=True)
        staged_source = stage / source.name
        shutil.copy2(source, staged_source)
        record['engine'] = compiler
        record['build_directory'] = str(stage.relative_to(root))
        env = os.environ.copy()
        if 'tectonic' in Path(compiler).name.lower():
            env.setdefault('TECTONIC_CACHE_DIR', str(root / 'tools/tectonic/cache'))
            cmd = [compiler, '--untrusted', '--keep-logs', '--keep-intermediates', '--outdir', str(stage), source.name]
            passes = 1
        else:
            cmd = [compiler, '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
                   '-file-line-error', '-output-directory=' + str(stage), source.name]
            passes = 2
        output = []
        record['compile_status'] = 'running'
        for _ in range(passes):
            completed = subprocess.run(cmd, cwd=stage, env=env, capture_output=True, timeout=300)
            output.append(completed.stdout.decode('utf-8', errors='replace') +
                          completed.stderr.decode('utf-8', errors='replace'))
            (folder / 'compile.log').write_text('\n'.join(output), encoding='utf-8')
            if completed.returncode:
                record['compile_status'] = 'failed'
                raise RuntimeError('LaTeX failed; see ' + str(folder / 'compile.log'))
        pdf = stage / (stem + '.pdf')
        if not pdf.is_file():
            raise RuntimeError('Compiler returned success without producing a PDF.')
        if digest(source) != record['source_sha256']:
            raise RuntimeError('Source changed during compilation; rebuild the latest source.')
        record['compile_status'] = 'passed'
        sys.path.insert(0, str(root / 'tools/python'))
        import pymupdf
        with pymupdf.open(pdf) as doc:
            for old_page in folder.glob('page-*.png'):
                if re.fullmatch(r'page-\d+\.png', old_page.name):
                    old_page.unlink()
            record['page_count'] = len(doc)
            record['one_page_status'] = ('passed' if len(doc) == 1 else 'needs_revision') if manifest['kind'] == 'Resume' else 'not_required'
            record['pages'] = []
            texts = []
            for i, page in enumerate(doc, 1):
                words = page.get_text('words')
                text = page.get_text(sort=True)
                texts.append(f'=== Page {i} ===\n{text}')
                page.get_pixmap(matrix=pymupdf.Matrix(1.4, 1.4)).save(str(folder / f'page-{i}.png'))
                record['pages'].append(dict(page=i, width_pt=page.rect.width, height_pt=page.rect.height,
                    word_count=len(words), text_bottom_pt=max((w[3] for w in words), default=0),
                    bottom_whitespace_pt=page.rect.height - max((w[3] for w in words), default=0)))
            (folder / 'extracted.txt').write_text('\n\n'.join(texts), encoding='utf-8')
            if not all(p['word_count'] for p in record['pages']):
                record['warnings'].append('One or more pages have no extractable words.')
        warnings = [line for line in '\n'.join(output).splitlines()
                    if any(x in line.lower() for x in ('overfull', 'underfull', 'warning', 'missing character'))]
        record['warnings'].extend(warnings)
        record['unified_diff'] = ''.join(difflib.unified_diff(
            (folder / 'initial.tex').read_text(encoding='utf-8').splitlines(True),
            source.read_text(encoding='utf-8').splitlines(True), fromfile=manifest['template'], tofile=source.name))
        destination = root / 'resumes/pdfs' / pdf.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, destination)
        record.update(pdf=str(destination.relative_to(root)), pdf_sha256=digest(destination),
                      status='compiled_pending_review')
        return record
    except Exception as exc:
        if record['compile_status'] == 'running':
            record['compile_status'] = 'failed'
        record['error'] = str(exc)
        record['warnings'].append('Any previously published PDF is not validated for this revision.')
        raise
    finally:
        record['template_unchanged_during_build'] = snapshot(root / 'template') == hashes
        paired(folder, 'validation', record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('--workspace', required=True, type=Path)
    prep.add_argument('--kind', required=True, choices=['CV', 'Resume'])
    prep.add_argument('--company', required=True)
    prep.add_argument('--title', required=True)
    comp = commands.add_parser('build')
    comp.add_argument('--workspace', required=True, type=Path)
    comp.add_argument('--stem', required=True)
    comp.add_argument('--engine')
    args = parser.parse_args()
    try:
        root = args.workspace.resolve()
        result = prepare(root, args.kind, args.company, args.title) if args.command == 'prepare' else build(root, args.stem, args.engine)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
