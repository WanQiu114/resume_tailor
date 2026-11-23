import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/resume-tailoring/scripts/resume_workflow.py'
spec = importlib.util.spec_from_file_location('workflow', SCRIPT)
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        folder = self.root / 'template'
        folder.mkdir()
        for name, text in [('resume.cls', 'class'), ('CV_template.tex', 'research'),
                           ('resume_template.tex', 'engineering')]:
            (folder / name).write_text(text, encoding='utf-8')
        self.original = workflow.snapshot(folder)

    def test_routing_collision_and_independent_dependencies(self):
        first = workflow.prepare(self.root, 'CV', 'A/B Corp', 'Research Scientist')
        second = workflow.prepare(self.root, 'CV', 'A/B Corp', 'Research Scientist')
        third = workflow.prepare(self.root, 'Resume', 'AB Corp', 'Software Engineer')
        self.assertEqual((self.root / first['source']).read_text(), 'research')
        self.assertEqual((self.root / third['source']).read_text(), 'engineering')
        self.assertTrue(second['task_id'].endswith('_02'))
        self.assertIn('AB_Corp', first['task_id'])
        (self.root / first['dependencies'] / 'resume.cls').write_text('edited copy')
        self.assertEqual((self.root / second['dependencies'] / 'resume.cls').read_text(), 'class')
        self.assertEqual(workflow.snapshot(self.root / 'template'), self.original)

    def test_failed_compile_does_not_claim_old_pdf_is_current(self):
        record = workflow.prepare(self.root, 'Resume', 'Test', 'Engineer')
        pdf = self.root / 'resumes/pdfs' / (record['task_id'] + '.pdf')
        pdf.parent.mkdir(parents=True)
        pdf.write_bytes(b'old PDF')
        with self.assertRaises(FileNotFoundError):
            workflow.build(self.root, record['task_id'], str(self.root / 'missing-engine.exe'))
        result = json.loads((self.root / 'resumes/reviews' / record['task_id'] / 'validation.jsonl').read_text())
        self.assertEqual(result['status'], 'failed')
        self.assertNotIn('pdf_sha256', result)
        self.assertEqual(pdf.read_bytes(), b'old PDF')
        self.assertEqual(workflow.snapshot(self.root / 'template'), self.original)

    def test_changed_template_stops_build(self):
        record = workflow.prepare(self.root, 'CV', 'Test', 'Researcher')
        (self.root / 'template/resume.cls').write_text('user edited')
        with self.assertRaisesRegex(RuntimeError, 'Template differs'):
            workflow.build(self.root, record['task_id'])


if __name__ == '__main__':
    unittest.main()
