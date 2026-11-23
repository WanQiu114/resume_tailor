"""Compile both user templates in an isolated build workspace, without tailoring."""
import importlib.util
from pathlib import Path
import shutil
import sys
import os

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools/python'))
spec = importlib.util.spec_from_file_location('workflow', ROOT / 'skills/resume-tailoring/scripts/resume_workflow.py')
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


def main():
    import tempfile
    os.environ['TECTONIC_CACHE_DIR'] = str(ROOT / 'tools/tectonic/cache')
    parent = ROOT / 'resumes/build'
    parent.mkdir(parents=True, exist_ok=True)
    isolated = Path(tempfile.mkdtemp(prefix='smoke-', dir=parent))
    before = workflow.snapshot(ROOT / 'template')
    shutil.copytree(ROOT / 'template', isolated / 'template')
    results = []
    for kind in ('Resume', 'CV'):
        manifest = workflow.prepare(isolated, kind, 'Template_Validation', 'Not_An_Application')
        try:
            result = workflow.build(isolated, manifest['task_id'], str(ROOT / 'tools/tectonic/tectonic.exe'))
        except Exception as exc:
            result = {'task_id': manifest['task_id'], 'status': 'failed', 'error': str(exc)}
        results.append(result)
        print(kind, result['status'], result.get('page_count', ''), flush=True)
        if kind == 'Resume' and result['status'] == 'failed':
            # Known source defect: standalone line-break command after a blank paragraph.
            # Repair only this isolated source; keep the failed raw-template result.
            source = isolated / manifest['source']
            text = source.read_text(encoding='utf-8')
            lines = text.splitlines(True)
            repaired = ''.join(line for line in lines if line.strip() != '\\\\')
            source.write_text(repaired, encoding='utf-8')
            try:
                fixed = workflow.build(isolated, manifest['task_id'], str(ROOT / 'tools/tectonic/tectonic.exe'))
            except Exception as exc:
                fixed = {'task_id': manifest['task_id'], 'status': 'failed', 'error': str(exc)}
            fixed['test_case'] = 'Resume copy with standalone line-break removed; no content tailoring'
            results.append(fixed)
            print('Resume syntax-only copy', fixed['status'], fixed.get('page_count', ''), flush=True)
    assert workflow.snapshot(ROOT / 'template') == before
    workflow.paired(ROOT / 'docs/changes', 'smoke-validation', {
        'task_id': 'resume-agent-001', 'isolated_workspace': str(isolated),
        'template_hashes': before, 'template_unchanged': True,
        'results': results, 'scope': 'Unmodified template compilation, not a tailored application; visual review pending.'})
    print(isolated, flush=True)


if __name__ == '__main__':
    main()
