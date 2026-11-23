"""Install this workspace's skill without overwriting another installation."""
import argparse
import json
import os
from pathlib import Path
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, help='Parent skill directory; default CODEX_HOME/skills')
    parser.add_argument('--update', action='store_true', help='Update only an installation bound to this workspace')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    parent = args.destination or Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills'
    destination = parent.resolve() / 'resume-tailoring'
    if destination.exists():
        config = destination / 'workspace.json'
        if not args.update or not config.is_file() or Path(json.loads(config.read_text(encoding='utf-8'))['workspace']).resolve() != root:
            parser.error('Destination exists or is bound elsewhere; use --update only for this workspace: ' + str(destination))
    shutil.copytree(root / 'skills/resume-tailoring', destination,
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc'), dirs_exist_ok=args.update)
    (destination / 'workspace.json').write_text(json.dumps({'workspace': str(root)}, indent=2) + '\n', encoding='utf-8')
    print(destination)
    print('Configured workspace: ' + str(root))
    sys.path.insert(0, str(root / 'skills/resume-tailoring/scripts'))
    from resume_workflow import paired, snapshot
    paired(root / 'docs/changes', 'installation', dict(task_id='resume-agent-001',
        destination=str(destination), workspace=str(root), status='installed', files=snapshot(destination),
        limitation='Selector visibility must be confirmed in a new Codex turn; this does not install a ChatGPT web plugin.'))


if __name__ == '__main__':
    main()
