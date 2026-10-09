"""Filesystem integration tests; all mutations stay in temporary directories."""

from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("manage", ROOT / "tools" / "manage.py")
manage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manage)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "source"
        # Small real skills preserve valid metadata and nested resources without
        # copying all scientific references for every conflict/rollback test.
        rows = [r for r in manage.load_catalog()
                if r["name"] in {"dft-vasp", "reading-contract", "ref-check"}]
        for row in rows:
            shutil.copytree(ROOT / "skills" / row["name"],
                            self.root / "skills" / row["name"])
        (self.root / "catalog.json").write_text(
            json.dumps({"skills": rows}, ensure_ascii=False), encoding="utf-8")
        self.target = self.base / "化学 research" / "skills"
        self.names = [r["name"] for r in manage.validate(self.root)]
        self.quiet = redirect_stdout(io.StringIO())
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)

    def apply(self, operation="install", names=None, **kw):
        manage.apply(self.root, self.target, names or self.names, operation, **kw)

    def test_install_idempotence_and_uninstall_preserve_unrelated_skill(self):
        unrelated = self.target / "personal-skill" / "SKILL.md"
        unrelated.parent.mkdir(parents=True)
        unrelated.write_text("private skill", encoding="utf-8")
        self.apply()
        before = manage.fingerprint(self.target)
        self.apply()
        self.assertEqual(before, manage.fingerprint(self.target))
        self.assertEqual(manage.status(self.root, self.target, self.names), 0)
        self.apply("uninstall")
        self.assertEqual(unrelated.read_text(encoding="utf-8"), "private skill")
        self.assertTrue(all(not (self.target / n).exists() for n in self.names))

    def test_full_catalog_roundtrip(self):
        names = [r["name"] for r in manage.validate(ROOT)]
        manage.apply(ROOT, self.target, names, "install")
        self.assertEqual(manage.status(ROOT, self.target, names), 0)
        manage.apply(ROOT, self.target, names, "uninstall")
        self.assertTrue(all(not (self.target / n).exists() for n in names))

    def test_preview_creates_no_target_or_backups(self):
        self.apply(dry_run=True)
        self.assertFalse(self.target.parent.exists())

    def test_conflict_is_preflighted_before_any_skill_is_written(self):
        name = self.names[-1]
        destination = self.target / name
        destination.mkdir(parents=True)
        (destination / "SKILL.md").write_text("unmanaged", encoding="utf-8")
        before = manage.fingerprint(self.target)
        with self.assertRaises(manage.Conflict):
            self.apply()
        self.assertEqual(before, manage.fingerprint(self.target))

    def test_local_edits_block_update_and_uninstall(self):
        self.apply()
        modified = self.target / self.names[0] / "SKILL.md"
        modified.write_text("local edit", encoding="utf-8")
        before = manage.fingerprint(self.target)
        for operation in ("install", "uninstall"):
            with self.assertRaises(manage.Conflict):
                self.apply(operation)
            self.assertEqual(before, manage.fingerprint(self.target))

    def test_replace_preserves_exact_old_files_in_backup(self):
        name = self.names[0]
        old = self.target / name
        old.mkdir(parents=True)
        (old / "SKILL.md").write_bytes(b"old local skill\r\n")
        (old / "notes.txt").write_bytes(b"keep my notes")
        fingerprint = manage.fingerprint(old)
        self.apply(names=[name], replace=True)
        backups = list((self.target.parent / ".llmskill-forchem-backups").iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual(manage.fingerprint(backups[0] / name), fingerprint)
        self.assertEqual(manage.fingerprint(old), manage.fingerprint(self.root / "skills" / name))

    def test_update_removes_obsolete_files_and_preserves_old_version(self):
        name = self.names[0]
        obsolete = self.root / "skills" / name / "obsolete.txt"
        obsolete.write_text("old resource", encoding="utf-8")
        self.apply()
        obsolete.unlink()
        source = self.root / "skills" / name / "SKILL.md"
        source.write_text(source.read_text(encoding="utf-8") + "\nNew instruction.\n", encoding="utf-8")
        self.assertEqual(manage.status(self.root, self.target, self.names), 1)
        self.apply()
        self.assertFalse((self.target / name / "obsolete.txt").exists())
        self.assertEqual(manage.status(self.root, self.target, self.names), 0)
        self.assertTrue(list((self.target.parent / ".llmskill-forchem-backups").glob(f"*/{name}/obsolete.txt")))

    def test_identical_unmanaged_install_can_be_adopted(self):
        name = self.names[0]
        shutil.copytree(self.root / "skills" / name, self.target / name)
        self.apply(names=[name])
        self.assertIn(name, manage.read_manifest(self.target)["skills"])

    def test_failed_manifest_write_rolls_back_existing_and_new_skills(self):
        self.apply(names=[self.names[0]])
        source = self.root / "skills" / self.names[0] / "SKILL.md"
        source.write_text(source.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        before = manage.fingerprint(self.target)
        with patch.object(manage, "write_manifest", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                self.apply()
        self.assertEqual(before, manage.fingerprint(self.target))

    def test_unmanaged_skill_cannot_be_uninstalled(self):
        name = self.names[0]
        shutil.copytree(self.root / "skills" / name, self.target / name)
        with self.assertRaises(manage.Conflict):
            self.apply("uninstall", names=[name])
        self.assertTrue((self.target / name / "SKILL.md").exists())

    def test_source_repository_cannot_be_installation_target(self):
        for target in (self.root, self.root / "skills", self.base):
            with self.assertRaises(manage.Conflict):
                manage.check_target(target, self.root)

    def test_symlinks_are_rejected_without_modifying_destination(self):
        actual = self.base / "actual"
        actual.mkdir()
        link = self.base / "link"
        try:
            link.symlink_to(actual, target_is_directory=True)
        except OSError:
            self.skipTest("This host does not permit creating symlinks")
        with self.assertRaises(manage.Conflict):
            manage.check_target(link, self.root)
        self.assertEqual(list(actual.iterdir()), [])

    def test_cli_roundtrip_uses_explicit_target(self):
        for command in ("install", "status", "uninstall"):
            result = subprocess.run(
                [sys.executable, str(ROOT / "tools" / "manage.py"), command,
                 "--target", str(self.target), "--skill", self.names[0]],
                capture_output=True, encoding="utf-8",
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_unknown_name_and_traversal_are_rejected(self):
        for name in ("unknown", "../outside"):
            with self.assertRaises(manage.Conflict):
                manage.select(manage.load_catalog(self.root), [name])

class SelectionTests(unittest.TestCase):
    def test_groups_and_explicit_skills_form_a_union(self):
        rows = manage.load_catalog()
        group = "research-evidence"
        expected = {r["name"] for r in rows if r.get("routing_group") == group}
        expected.add("scientific-skill-router")
        actual = manage.select(rows, ["scientific-skill-router"], [group, group])
        self.assertEqual(actual, sorted(expected))
        with self.assertRaises(manage.Conflict):
            manage.select(rows, None, ["misspelled-group"])

    def test_search_matches_chinese_and_english_and_preserves_sources(self):
        for query, expected in [("VASP", "mat-dft-vasp"), ("晶体", "pymatgen")]:
            result = subprocess.run(
                [sys.executable, str(ROOT / "tools/manage.py"), "list", "--search", query],
                capture_output=True, encoding="utf-8")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(expected, result.stdout)
            self.assertIn("https://github.com/", result.stdout)

    def test_invalid_search_cannot_accidentally_install_all_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "not-created"
            result = subprocess.run(
                [sys.executable, str(ROOT / "tools/manage.py"), "install",
                 "--search", "VASP", "--target", str(target)],
                capture_output=True, encoding="utf-8")
            self.assertEqual(result.returncode, 2)
            self.assertFalse(target.exists())

    def test_unknown_group_fails_before_writing_and_preview_is_exact(self):
        rows = manage.load_catalog()
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "not-created"
            base = [sys.executable, str(ROOT / "tools/manage.py"), "install",
                    "--target", str(target)]
            result = subprocess.run(base + ["--group", "typo"],
                                    capture_output=True, encoding="utf-8")
            self.assertEqual(result.returncode, 2)
            self.assertFalse(target.exists())
            result = subprocess.run(base + ["--group", "runtime-support", "--dry-run"],
                                    capture_output=True, encoding="utf-8")
            self.assertEqual(result.returncode, 0, result.stderr)
            selected = {line.removeprefix("install: ") for line in result.stdout.splitlines()
                        if line.startswith("install: ")}
            self.assertEqual(selected, {r["name"] for r in rows
                                        if r.get("routing_group") == "runtime-support"})
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
