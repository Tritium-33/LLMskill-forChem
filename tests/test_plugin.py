"""Packaging and first-install safeguards; no network or real home writes."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


builder = module("build_plugin")
installer = module("install_plugin")


class PluginPackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.bundle = builder.build(ROOT, self.base / "bundle")

    def tearDown(self):
        self.tmp.cleanup()

    def test_bundle_keeps_canonical_bytes_and_excludes_private_sources(self):
        data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual({p.name for p in (self.bundle / "skills").iterdir()},
                         {s["name"] for s in data["skills"]} | {"chem-skill-panel"})
        for s in data["skills"]:
            for p in (ROOT / "skills" / s["name"]).rglob("*"):
                if p.is_file():
                    relative = p.relative_to(ROOT)
                    self.assertEqual(p.read_bytes(), (self.bundle / relative).read_bytes())
        html = (self.bundle / "assets/panel.html").read_text(encoding="utf-8")
        self.assertNotIn("__CHEM_CATALOG_JSON__", html)
        self.assertNotIn(str(Path.home()), html)
        self.assertNotIn('"thread_id"', html)

    def test_builder_does_not_replace_unmanaged_directory(self):
        target = self.base / "personal"
        target.mkdir()
        (target / "keep.txt").write_text("keep")
        with self.assertRaises(ValueError):
            builder.build(ROOT, target)
        self.assertEqual((target / "keep.txt").read_text(), "keep")

    def test_dry_run_writes_nothing(self):
        target = self.base / "user"
        result = installer.install(self.bundle, target, dry_run=True)
        self.assertTrue(result["dry_run"])
        self.assertFalse(target.exists())

    def test_marketplace_preserves_existing_entries_and_name(self):
        old = {"name": "my-personal", "interface": {"displayName": "My collection"},
               "plugins": [{"name": "unrelated", "source": "./plugins/unrelated"}]}
        new = installer.marketplace_with_plugin(old)
        self.assertEqual(new["name"], old["name"])
        self.assertEqual(new["interface"], old["interface"])
        self.assertEqual(new["plugins"][0], old["plugins"][0])
        self.assertEqual(len(old["plugins"]), 1)
        with self.assertRaises(ValueError):
            installer.marketplace_with_plugin(new)

    def test_existing_target_stops_before_dependency_install(self):
        home = self.base / "user"
        target = home / "plugins/chem-skill-panel"
        target.mkdir(parents=True)
        (target / "keep.txt").write_text("keep")
        with patch.object(installer.subprocess, "run") as run:
            with self.assertRaises(ValueError):
                installer.install(self.bundle, home)
            run.assert_not_called()
        self.assertEqual((target / "keep.txt").read_text(), "keep")

    def test_dependency_failure_preserves_marketplace(self):
        home = self.base / "user"
        market = home / ".agents/plugins/marketplace.json"
        market.parent.mkdir(parents=True)
        original = '{"name":"personal","plugins":[]}\n'
        market.write_text(original)
        def fail(command, **kwargs):
            runtime = home / "plugins/.chem-skill-panel-runtime"
            runtime.mkdir()
            raise OSError("simulated dependency failure")
        with patch.object(installer.subprocess, "run", side_effect=fail):
            with self.assertRaises(OSError):
                installer.install(self.bundle, home)
        self.assertEqual(market.read_text(), original)
        self.assertFalse((home / "plugins/chem-skill-panel").exists())
        self.assertFalse((home / "plugins/.chem-skill-panel-runtime").exists())
        self.assertFalse((market.parent / ".chem-skill-panel-install.lock").exists())


if __name__ == "__main__":
    unittest.main()
