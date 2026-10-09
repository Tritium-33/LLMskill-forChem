#!/usr/bin/env python3
"""Install a built chem-skill-panel into this OS user's personal marketplace.

Run the copy named install.py inside the built plugin directory.
Never edits the canonical repository or silently replaces another installation.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

NAME = "chem-skill-panel"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        tmp = Path(handle.name)
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    try:
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def marketplace_with_plugin(market: dict) -> dict:
    if not isinstance(market, dict) or not re.fullmatch(r"[A-Za-z0-9_-]+", str(market.get("name", ""))):
        raise ValueError("Invalid marketplace name")
    result = json.loads(json.dumps(market))
    entries = result.setdefault("plugins", [])
    if not isinstance(entries, list):
        raise ValueError("Invalid marketplace plugins list")
    if any(isinstance(p, dict) and p.get("name") == NAME for p in entries):
        raise ValueError("Plugin already registered. Use Codex's update/reinstall workflow; no entry was overwritten.")
    entries.append({"name": NAME, "source": {"source": "local", "path": f"./plugins/{NAME}"},
                    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                    "category": "Productivity"})
    return result


def configure_mcp(target: Path, python: Path) -> None:
    # Absolute paths are produced only at installation time, for the actual OS.
    atomic_json(target / ".mcp.json", {"mcpServers": {NAME: {
        "command": str(python), "args": [str(target / "scripts/server.py")],
        "env": {"PYTHONUTF8": "1"}
    }}})
    manifest_path = target / ".codex-plugin/plugin.json"
    manifest = read_json(manifest_path)
    manifest["mcpServers"] = "./.mcp.json"
    atomic_json(manifest_path, manifest)


def install(source: Path, user_root: Path, *, dry_run: bool = False) -> dict:
    source = source.resolve()
    marker = source / ".chem-skill-panel-build.json"
    if not marker.is_file() or read_json(marker).get("package") != NAME:
        raise ValueError("Run install.py inside a built plugin package. Build the package first.")
    user_root = user_root.absolute()
    target = user_root / "plugins" / NAME
    runtime = user_root / "plugins" / ".chem-skill-panel-runtime"
    market_path = user_root / ".agents/plugins/marketplace.json"
    for path in (target, runtime, market_path):
        for ancestor in [path, *path.parents]:
            if ancestor.is_symlink() or getattr(ancestor, "is_junction", lambda: False)():
                raise ValueError(f"Refusing symlink/junction install path: {ancestor}")
    if target.exists() or runtime.exists():
        raise ValueError("A plugin or runtime already exists; nothing was replaced. See the update instructions.")
    current = read_json(market_path) if market_path.exists() else {
        "name": "personal", "interface": {"displayName": "Personal"}, "plugins": []}
    next_market = marketplace_with_plugin(current)
    result = {"plugin": str(target), "runtime": str(runtime), "marketplace": str(market_path),
              "marketplace_name": current["name"], "dry_run": dry_run}
    if dry_run:
        return result
    market_path.parent.mkdir(parents=True, exist_ok=True)
    lock = market_path.parent / ".chem-skill-panel-install.lock"
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    os.close(fd)
    copied = False
    runtime_started = False
    try:
        # Re-check after acquiring our installation lock.
        latest = read_json(market_path) if market_path.exists() else current
        if latest != current or target.exists() or runtime.exists():
            raise ValueError("Installation paths changed; retry after inspecting them.")
        target.parent.mkdir(parents=True, exist_ok=True)
        runtime_started = True
        subprocess.run([sys.executable, "-m", "venv", str(runtime)], check=True)
        python = runtime / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        subprocess.run([str(python), "-m", "pip", "install", "-r", str(source / "requirements.txt")], check=True)
        copied = True
        shutil.copytree(source, target)
        configure_mcp(target, python)
        if market_path.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            shutil.copy2(market_path, market_path.with_name(f"marketplace.json.backup-{stamp}"))
        atomic_json(market_path, next_market)
    except BaseException:
        if copied and target.exists():
            shutil.rmtree(target)
        if runtime_started and runtime.exists():
            shutil.rmtree(runtime)
        raise
    finally:
        lock.unlink(missing_ok=True)
    result["view_url"] = f"codex://plugins/{NAME}?marketplacePath={quote(str(market_path), safe='')}"
    return result


def main() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10+ is required. Use a newer Python interpreter.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--user-root", type=Path, default=Path.home(),
                        help="Override only for isolated testing; default is this OS user's home")
    args = parser.parse_args()
    try:
        result = install(Path(__file__).resolve().parent, args.user_root, dry_run=args.dry_run)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Installation stopped: {error}") from error
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not args.dry_run:
        print("Registered in the personal marketplace. Open Codex's Plugins screen to install, then start a new chat.")


if __name__ == "__main__":
    main()
