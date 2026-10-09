"""Integration evidence for declared routes and actual bundled table CLIs.

These checks do not evaluate an LLM's routing or validate VASP/scientific claims.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / (name + '.py'))
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


architecture = module('check_architecture')
audit = module('audit_dependencies')


class ArchitectureTests(unittest.TestCase):
    def test_references_resolve(self):
        summary = architecture.validate()
        self.assertEqual(summary['cases'], 11)
        self.assertEqual(summary['workflows'], 3)

    def test_unknown_skill_and_escape_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copy2(ROOT / 'catalog.json', root / 'catalog.json')
            shutil.copytree(ROOT / 'skills/dft-vasp', root / 'skills/dft-vasp')
            shutil.copytree(ROOT / 'skills/scientific-skill-router/references',
                            root / 'skills/scientific-skill-router/references')
            shutil.copytree(ROOT / 'examples', root / 'examples')
            path = root / 'catalog.json'
            data = json.loads(path.read_text(encoding='utf-8'))
            row = next(r for r in data['skills'] if 'capability' in r)
            row['capability']['relations']['feeds_into'].append('nonexistent-skill')
            path.write_text(json.dumps(data), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'relation'):
                architecture.validate(root)
            row['capability']['relations']['feeds_into'].pop()
            path.write_text(json.dumps(data), encoding='utf-8')
            case_path = root / 'examples/cases.json'
            cases = json.loads(case_path.read_text(encoding='utf-8'))
            cases['cases'][0]['inputs'] = ['../catalog.json']
            case_path.write_text(json.dumps(cases), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'escaping'):
                architecture.validate(root)

    def test_inventory_exposes_external_backend_without_importing_it(self):
        report = audit.inventory()
        self.assertEqual(len(report['skills']), 53)
        row = next(r for r in report['skills'] if r['name'] == 'mat-dft-vasp')
        self.assertIn('src.utils.dft.vasp_parser', row['external_import_candidates'])
        self.assertEqual(row['runtime_status'], 'not_checked')
        self.assertEqual(row['parse_errors'], [])


@unittest.skipIf(sys.version_info < (3, 11), 'Upstream EDA core declares Python 3.11+')
class TableExecutionTests(unittest.TestCase):
    def run_cli(self, filename, script='tabular_profile.py', extra=()):
        fixture = ROOT / 'examples/fixtures/tables' / filename
        before = hashlib.sha256(fixture.read_bytes()).hexdigest()
        command = [sys.executable, '-X', 'warn_default_encoding', '-W', 'error::EncodingWarning',
                   str(ROOT / 'skills/exploratory-data-analysis/scripts' / script),
                   str(fixture), '--root', str(fixture.parent), *extra]
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', timeout=30)
        self.assertEqual(hashlib.sha256(fixture.read_bytes()).hexdigest(), before)
        return result

    def test_clean_profile_known_counts_and_mean(self):
        result = self.run_cli('clean.csv')
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)['analysis']
        self.assertEqual((data['rows_scanned'], data['column_count']), (4, 5))
        self.assertFalse(data['row_limit_reached'])
        self.assertEqual(sum(c['missing_count'] for c in data['columns']), 0)
        self.assertAlmostEqual(data['columns'][4]['numeric_aggregates']['mean'], 1.05)

    def test_missing_values_not_imputed(self):
        result = self.run_cli('missing.csv')
        self.assertEqual(result.returncode, 0, result.stderr)
        columns = json.loads(result.stdout)['analysis']['columns']
        self.assertEqual([c['missing_count'] for c in columns], [0, 0, 0, 1, 1])
        self.assertEqual(columns[4]['non_missing_count'], 3)

    def test_malformed_table_rejected(self):
        result = self.run_cli('malformed.csv')
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('"profile_type"', result.stdout)

    def test_group_overlap_positive_and_negative_controls(self):
        for fixture, expected in [('group-leakage.csv', 2), ('clean.csv', 0)]:
            with self.subTest(fixture=fixture):
                result = self.run_cli(fixture, 'missingness_leakage_audit.py',
                                      ('--group-column', 'group', '--split-column', 'split'))
                self.assertEqual(result.returncode, 0, result.stderr)
                data = json.loads(result.stdout)['analysis']['leakage_audit']
                self.assertEqual(data['group_tokens_in_multiple_splits'], expected)
                self.assertFalse(data['tracking_truncated'])
