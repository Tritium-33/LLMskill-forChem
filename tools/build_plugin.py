#!/usr/bin/env python3
"""Build a standalone plugin from the canonical catalog and skill sources."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parents[1]
NAME = "chem-skill-panel"
MARKER = ".chem-skill-panel-build.json"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build(repo: Path, destination: Path) -> Path:
    repo = repo.resolve()
    destination = destination.absolute()
    if destination.is_symlink() or (destination.exists() and not (destination / MARKER).is_file()):
        raise ValueError("Output exists and is not a generated plugin; refusing to replace it.")
    data = json.loads((repo / "catalog.json").read_text(encoding="utf-8"))
    names = [s["name"] for s in data["skills"]]
    if not names or len(set(names)) != len(names) or not all(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", n) for n in names):
        raise ValueError("Invalid or duplicate catalog skill names")
    if NAME in names:
        raise ValueError("The panel entrypoint must not shadow a catalog skill")
    source = repo / "plugins" / NAME
    for tree in [source, *(repo / "skills" / n for n in names)]:
        if not tree.is_dir() or tree.is_symlink() or any(p.is_symlink() for p in tree.rglob("*")):
            raise ValueError(f"Missing source or unsupported symlink: {tree}")
    for item in data["skills"]:
        provenance = json.loads((repo / "skills" / item["name"] / "SOURCE.json").read_text(encoding="utf-8"))
        if provenance.get("kind") == "original":
            item["source"] = {"name": "LLMskill-forChem (original)", "url": None}
            continue
        repository = provenance["repository"].rstrip("/")
        if not re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ValueError("Expected an HTTPS GitHub source repository")
        item["source"] = {
            "name": repository.removeprefix("https://github.com/"),
            "url": f"{repository}/blob/{quote(provenance['commit'], safe='')}/{quote(provenance['path'], safe='/')}/SKILL.md",
        }
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="chem-plugin-build-", dir=destination.parent) as tmp:
        stage = Path(tmp) / NAME
        shutil.copytree(source, stage, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        for name in names:
            shutil.copytree(repo / "skills" / name, stage / "skills" / name)
        for name in ["catalog.json", "LICENSE", "THIRD_PARTY_NOTICES.md"]:
            shutil.copy2(repo / name, stage / name)
        write_json(stage / "catalog.json", data)
        shutil.copy2(repo / "tools/install_plugin.py", stage / "install.py")
        shutil.copy2(repo / "docs/codex-plugin.md", stage / "README.md")
        template = stage / "assets/panel.template.html"
        raw = json.dumps(data, ensure_ascii=False).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
        html = template.read_text(encoding="utf-8").replace("__CHEM_CATALOG_JSON__", raw)
        (stage / "assets/panel.html").write_text(html, encoding="utf-8")
        template.unlink()
        for launcher in stage.glob("*.cmd"):
            launcher.write_bytes(launcher.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8"))
        write_json(stage / MARKER, {"package": NAME, "version": "0.1.0", "skills": names})
        if destination.exists():
            previous = Path(tmp) / "previous"
            destination.rename(previous)
            try:
                stage.rename(destination)
            except BaseException:
                previous.rename(destination)
                raise
        else:
            stage.rename(destination)
    return destination


def main() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10+ is required. Use a newer Python interpreter.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=REPO / "dist" / NAME)
    parser.add_argument("--zip", action="store_true", help="Also create a portable ZIP")
    args = parser.parse_args()
    target = build(REPO, args.output)
    print(f"Built: {target}")
    print(f"Browser panel: {target / 'assets/panel.html'}")
    if args.zip:
        archive = shutil.make_archive(str(target), "zip", target.parent, target.name)
        print(f"ZIP: {archive}")


if __name__ == "__main__":
    main()
