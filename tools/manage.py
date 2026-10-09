#!/usr/bin/env python3
"""Manage this repository's skill copies. Python 3.10+, standard library only."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ".llmskill-forchem.json"
LOCK = ".llmskill-forchem.lock"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class Conflict(Exception):
    """An operation would overwrite data without sufficient provenance."""


def is_link(path):
    """Include Windows junctions/reparse points on Python versions before 3.12."""
    if path.is_symlink():
        return True
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
    except FileNotFoundError:
        return False
    return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def load_catalog(root=ROOT):
    data = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    rows = data["skills"]
    names = [row["name"] for row in rows]
    if len(names) != len(set(names)) or not all(NAME.fullmatch(n) for n in names):
        raise Conflict("Invalid or duplicate skill names in catalog.json")
    return rows


def fingerprint(directory):
    """Hash exact bytes; reject links and special files before copying/removing."""
    if is_link(directory) or (directory.exists() and not directory.is_dir()):
        raise Conflict(f"Expected a regular directory: {directory}")
    if not directory.exists():
        return None
    result = {}
    for path in sorted(directory.rglob("*")):
        if is_link(path) or (not path.is_file() and not path.is_dir()):
            raise Conflict(f"Links and special files are not managed: {path}")
        if path.is_file():
            result[path.relative_to(directory).as_posix()] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
    return result


def validate(root=ROOT):
    rows = load_catalog(root)
    expected = {r["name"] for r in rows}
    actual = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    if expected != actual:
        raise Conflict("catalog.json and skills/ directories differ")
    for row in rows:
        folder = root / "skills" / row["name"]
        files = fingerprint(folder)
        for required in ("SKILL.md", "SOURCE.json", "LICENSE", "agents/openai.yaml"):
            if required not in files:
                raise Conflict(f"Missing {row['name']}/{required}")
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            raise Conflict(f"Missing skill frontmatter: {row['name']}")
        # These bundled skills use simple, single-line metadata, not general YAML.
        fields = dict(line.split(":", 1) for line in parts[1].splitlines() if ":" in line)
        if fields.get("name", "").strip() != row["name"] or not fields.get("description", "").strip():
            raise Conflict(f"Invalid skill metadata: {row['name']}")
        source = json.loads((folder / "SOURCE.json").read_text(encoding="utf-8"))
        if source.get("kind") == "original":
            if source.get("project") != "LLMskill-forChem" or source.get("path") != f"skills/{row['name']}" or not source.get("version"):
                raise Conflict(f"Invalid original-skill provenance: {row['name']}")
            continue
        if not re.fullmatch(r"[0-9a-f]{40}", source.get("commit", "")):
            raise Conflict(f"Missing pinned upstream commit: {row['name']}")
        if not source.get("repository", "").startswith("https://github.com/"):
            raise Conflict(f"Missing upstream repository: {row['name']}")
    return rows


def check_target(target, root=ROOT):
    target = target.expanduser().absolute()
    # Resolving a pre-existing symlink would hide which location is being changed.
    for path in (target, *target.parents):
        if is_link(path):
            raise Conflict(f"Choose a target without symlink/junction ancestors: {path}")
    resolved, source = target.resolve(), root.resolve()
    if resolved == source or resolved in source.parents or source in resolved.parents:
        raise Conflict("Installation target must be outside this source repository")
    if target.exists() and not target.is_dir():
        raise Conflict(f"Target is not a directory: {target}")
    return target


def read_manifest(target):
    path = target / MANIFEST
    if is_link(path):
        raise Conflict(f"Manifest cannot be a symlink: {path}")
    if not path.exists():
        return {"schema_version": 1, "package": "LLMskill-forChem", "skills": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("package") != "LLMskill-forChem":
        raise Conflict("Unrecognized installation manifest; leave it untouched")
    if not isinstance(data.get("skills"), dict):
        raise Conflict("Invalid installation manifest")
    return data


def write_manifest(target, data):
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=target,
                                     prefix=".llmskill-", suffix=".tmp", delete=False) as f:
        path = Path(f.name)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    try:
        path.replace(target / MANIFEST)
    finally:
        path.unlink(missing_ok=True)


@contextmanager
def locked(target):
    target.mkdir(parents=True, exist_ok=True)
    lock = target / LOCK
    try:
        lock.mkdir()
    except FileExistsError as exc:
        raise Conflict(f"Another operation may be running; inspect lock: {lock}") from exc
    try:
        yield
    finally:
        lock.rmdir()


def select(rows, names, groups=None):
    known = {r["name"] for r in rows}
    known_groups = {r.get("routing_group") for r in rows} - {None}
    if set(groups or []) - known_groups:
        raise Conflict("Unknown group(s): " + ", ".join(sorted(set(groups) - known_groups)))
    chosen = set(names or [])
    if groups:
        chosen.update(r["name"] for r in rows if r.get("routing_group") in groups)
    selected = sorted(chosen if names or groups else known)
    if set(selected) - known:
        raise Conflict("Unknown skill(s): " + ", ".join(sorted(set(selected) - known)))
    return selected


def plan(root, target, names, operation, replace=False):
    state = read_manifest(target)
    actions = []
    for name in names:
        current = fingerprint(target / name)
        desired = fingerprint(root / "skills" / name)
        previous = state["skills"].get(name)
        if operation == "uninstall":
            if previous is None:
                if current is not None:
                    raise Conflict(f"Unmanaged skill will not be removed: {name}")
                action = "absent"
            elif current is not None and current != previous["files"]:
                raise Conflict(f"Locally changed skill will not be removed: {name}")
            else:
                action = "remove" if current is not None else "forget"
        elif current == desired:
            action = "unchanged" if previous and previous["files"] == desired else "adopt"
        elif current is None:
            action = "install"
        elif previous and current == previous["files"]:
            action = "update"
        elif replace:
            action = "replace-with-backup"
        else:
            raise Conflict(f"Existing unmanaged or locally changed skill: {name}. "
                           "Review it first; --replace installs the source after backing it up.")
        actions.append((name, action, current, desired))
    return state, actions


def apply(root, target, names, operation, replace=False, dry_run=False):
    """Preflight all skills; back up and roll back if a filesystem operation fails."""
    if dry_run:
        _, actions = plan(root, target, names, operation, replace)
        for name, action, _, _ in actions:
            print(f"{action}: {name}")
        return
    with locked(target):
        state, actions = plan(root, target, names, operation, replace)
        changes = [a for a in actions if a[1] not in ("unchanged", "absent")]
        if not changes:
            print("No changes.")
            return
        backup_parent = target.parent / ".llmskill-forchem-backups"
        if is_link(backup_parent):
            raise Conflict("Backup directory cannot be a symlink")
        backup = backup_parent / uuid.uuid4().hex
        backup.mkdir(parents=True)
        old_manifest = target / MANIFEST
        had_manifest = old_manifest.exists()
        if had_manifest:
            shutil.copy2(old_manifest, backup / MANIFEST)
        for name, _, current, _ in changes:
            if current is not None:
                shutil.copytree(target / name, backup / name)
        touched = []
        try:
            with tempfile.TemporaryDirectory(prefix=".llmskill-stage-", dir=target) as tmp:
                staging = Path(tmp)
                if operation == "install":
                    for name, action, _, _ in changes:
                        if action != "adopt":
                            shutil.copytree(root / "skills" / name, staging / name)
                for name, action, current, desired in changes:
                    destination = target / name
                    if fingerprint(destination) != current:
                        raise Conflict(f"Skill changed during installation: {name}")
                    if action not in ("adopt", "forget"):
                        touched.append(name)
                        if destination.exists():
                            shutil.rmtree(destination)
                        if operation == "install":
                            (staging / name).rename(destination)
                    if operation == "install":
                        state["skills"][name] = {"files": desired}
                    else:
                        state["skills"].pop(name, None)
                write_manifest(target, state)
        except BaseException:
            for name in reversed(touched):
                destination = target / name
                if destination.exists():
                    shutil.rmtree(destination)
                if (backup / name).exists():
                    shutil.copytree(backup / name, destination)
            if had_manifest:
                shutil.copy2(backup / MANIFEST, old_manifest)
            else:
                old_manifest.unlink(missing_ok=True)
            raise
        for name, action, _, _ in actions:
            print(f"{action}: {name}")
        print(f"Backup: {backup}")


def status(root, target, names):
    state = read_manifest(target)
    dirty = False
    for name in names:
        current = fingerprint(target / name)
        desired = fingerprint(root / "skills" / name)
        previous = state["skills"].get(name)
        if current is None:
            label = "missing"
        elif current == desired:
            label = "current" if previous and previous["files"] == desired else "identical-unmanaged"
        elif previous and current == previous["files"]:
            label = "update-available"
        else:
            label = "local-change-or-conflict"
        print(f"{label}: {name}")
        dirty |= label != "current"
    return int(dirty)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("list", "check", "install", "status", "uninstall"))
    parser.add_argument("--target", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Exact skills directory; default: ~/.agents/skills")
    parser.add_argument("--skill", action="append", help="Select a skill; repeatable; default: all")
    parser.add_argument("--group", action="append",
                        help="Select a functional group; repeatable, combined with --skill")
    parser.add_argument("--search", help="Filter list by English name or Chinese purpose")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--replace", action="store_true", help="Install over conflicts, with backup")
    args = parser.parse_args(argv)
    try:
        rows = validate()
        if args.search is not None and args.command != "list":
            raise Conflict("--search is only supported for list; use --skill or --group to install")
        if args.replace and args.command != "install":
            raise Conflict("--replace is only supported for install")
        if args.command == "check":
            if args.skill or args.group:
                raise Conflict("check validates the complete source catalog; do not pass selectors")
            print(f"OK: {len(rows)} skills; metadata, provenance and required files checked.")
            return 0
        names = select(rows, args.skill, args.group)
        if args.command == "list":
            query = (args.search or "").strip().casefold()
            matches = [r for r in rows if r["name"] in names and
                       query in (r["name"] + " " + r["summary"]).casefold()]
            for row in matches:
                source = json.loads((ROOT / "skills" / row["name"] / "SOURCE.json").read_text(encoding="utf-8"))
                origin = source.get("repository", source.get("project", "Local"))
                print(f"{row['name']} | {row['summary']}\n  {row.get('routing_group', 'router')} | {origin}")
            if not matches:
                print("No matching skills. / 没有匹配的技能。")
                return 1
            return 0
        target = check_target(args.target)
        print(f"Target: {target}")
        if args.command == "status":
            return status(ROOT, target, names)
        apply(ROOT, target, names, args.command, args.replace, args.dry_run)
        return 0
    except (Conflict, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    # Windows consoles may use a legacy encoding; keep Chinese catalog text readable.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    sys.exit(main())
