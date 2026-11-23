"""Download a pinned official Windows Tectonic binary into this workspace."""
import hashlib
import json
from pathlib import Path
import sys
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/resume-tailoring/scripts'))
from resume_workflow import paired


def main():
    folder = ROOT / 'tools/tectonic'
    folder.mkdir(parents=True, exist_ok=True)
    if (folder / 'tectonic.exe').exists():
        raise SystemExit('Tectonic already exists; no overwrite performed.')
    version = '0.17.0'
    req = urllib.request.Request(
        f'https://api.github.com/repos/tectonic-typesetting/tectonic/releases/tags/tectonic%40{version}',
        headers={'User-Agent': 'resume-tailoring-setup'})
    with urllib.request.urlopen(req, timeout=60) as response:
        release = json.load(response)
    asset = next(a for a in release['assets'] if a['name'] == f'tectonic-{version}-x86_64-pc-windows-msvc.zip')
    archive = folder / asset['name']
    with urllib.request.urlopen(asset['browser_download_url'], timeout=60) as response:
        archive.write_bytes(response.read())
    sha = hashlib.sha256(archive.read_bytes()).hexdigest()
    upstream = asset.get('digest')
    if upstream and upstream != 'sha256:' + sha:
        raise SystemExit('Release digest mismatch; binary not extracted.')
    with zipfile.ZipFile(archive) as bundle:
        executable = next(n for n in bundle.namelist() if Path(n).name == 'tectonic.exe')
        (folder / 'tectonic.exe').write_bytes(bundle.read(executable))
    paired(ROOT / 'docs/changes', 'tooling', dict(
        task_id='resume-agent-001', version=version, url=asset['browser_download_url'],
        archive_sha256=sha, upstream_digest=upstream,
        upstream_digest_verified=bool(upstream), installation='tools/tectonic/tectonic.exe'))
    print(folder / 'tectonic.exe')


if __name__ == '__main__':
    main()
