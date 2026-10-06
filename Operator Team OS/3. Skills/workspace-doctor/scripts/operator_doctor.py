#!/usr/bin/env python3
"""Read-only health checks for a portable Operator OS workspace."""

from __future__ import annotations

import json
import hashlib
import re
import subprocess
from pathlib import Path

REQUIRED = [
    "AGENTS.md", "README.md", "SETUP.md",
    "Operator Team OS/AGENTS.md", "Operator Team OS/WIKI.md",
    "Operator Team OS/VERSION", "Operator Team OS/CHANGELOG.md",
    "Operator Team OS/1. SOPs/knowledge-graph-schema.md",
    "Operator Team OS/3. Skills/memory-read/SKILL.md",
    "Operator Team OS/3. Skills/memory-manage/SKILL.md",
    "Operator Team OS/4. Workflows/memory.md",
    "Operator Team OS/6. Memory/ACTIVE.md",
    "Operator Team OS/6. Memory/LONG_TERM.md",
    "Operator Team OS/6. Memory/logs",
    "Operator Team OS/6. Memory/proposals",
]
POINTERS = ["AGENTS.md"]
# A CLAUDE.md makes Claude Code ignore AGENTS.md; GEMINI.md is unnecessary duplication.
LEGACY_POINTERS = ["CLAUDE.md", "GEMINI.md"]
CORE_TEXT = [
    "AGENTS.md", "README.md", "SETUP.md",
    "Operator Team OS/AGENTS.md", "Operator Team OS/WIKI.md",
]


def release_sources(root: Path) -> list[Path]:
    os_root = root / "Operator Team OS"
    files = [os_root / "AGENTS.md", os_root / "VERSION"]
    files += sorted((os_root / "2. Agents").glob("*.md"))
    files += sorted((os_root / "3. Skills").glob("*/SKILL.md"))
    files += sorted((os_root / "4. Workflows").glob("*.md"))
    return files


def release_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in release_sources(root):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def frontmatter_keys(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return set()
    block = text[4:].split("\n---\n", 1)[0]
    return {match.group(1) for line in block.splitlines() if (match := re.match(r"^([a-zA-Z][\w-]*):", line))}


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    checks: list[tuple[bool, str]] = []
    for name in REQUIRED:
        checks.append(((root / name).exists(), f"required: {name}"))
    for name in POINTERS:
        path = root / name
        checks.append((path.exists() and not path.is_symlink(), f"portable pointer: {name}"))
    legacy = [name for name in LEGACY_POINTERS if (root / name).exists()]
    checks.append((not legacy, "no legacy per-tool instruction files" + (f": {', '.join(legacy)}" if legacy else "")))
    version = (root / "Operator Team OS/VERSION").read_text().strip()
    checks.append((bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), "semantic VERSION"))

    manifest = root / "Operator Team OS/MANIFEST.json"
    try:
        data = json.loads(manifest.read_text())
        checks.append((data.get("os_version") == version, "manifest version matches VERSION"))
        checks.append((data.get("source_hash") == release_hash(root), "manifest source hash is current"))
    except (OSError, json.JSONDecodeError):
        checks.append((False, "valid MANIFEST.json"))

    machine_path = re.compile(r"(?:/Users/[^/\s]+|/home/[^/\s]+|[A-Za-z]:\\\\Users\\\\[^\\\s]+)")
    offenders = []
    for name in CORE_TEXT:
        path = root / name
        if path.exists() and machine_path.search(path.read_text(encoding="utf-8", errors="replace")):
            offenders.append(name)
    checks.append((not offenders, "no machine-specific paths in core docs" + (f": {', '.join(offenders)}" if offenders else "")))

    linked_roots = [root / ".agent"]
    symlinks = [path.relative_to(root).as_posix() for base in linked_roots if base.exists() for path in base.rglob("*") if path.is_symlink()]
    checks.append((not symlinks, "no cloud-fragile platform symlinks" + (f": {', '.join(symlinks)}" if symlinks else "")))

    schemas = [
        (root / "Operator Team OS/1. SOPs", {"type", "title", "owner", "status", "last-reviewed", "tags"}),
        (root / "Operator Team OS/2. Agents", {"type", "title", "domain", "status", "tags"}),
        (root / "Operator Team OS/4. Workflows", {"type", "triggers", "requires", "status", "tags", "description"}),
    ]
    metadata_gaps = []
    for folder, required in schemas:
        for path in folder.glob("*.md"):
            missing = required - frontmatter_keys(path)
            if missing:
                metadata_gaps.append(f"{path.name}({','.join(sorted(missing))})")
    checks.append((not metadata_gaps, "core frontmatter schema" + (f": {'; '.join(metadata_gaps)}" if metadata_gaps else "")))

    try:
        tracked = subprocess.check_output(["git", "ls-files"], cwd=root, text=True).splitlines()
        forbidden = [
            name for name in tracked
            if Path(name).name != ".gitkeep"
            and any(part.lower() in {"node_modules", ".venv", "__pycache__", "z_temp"} for part in Path(name).parts)
        ]
        checks.append((not forbidden, "no tracked dependency/cache/temp files" + (f": {len(forbidden)}" if forbidden else "")))
    except (OSError, subprocess.CalledProcessError):
        checks.append((True, "Git tracking check skipped"))

    failed = 0
    for passed, label in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {label}")
        failed += not passed
    print(f"\n{len(checks) - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
