#!/usr/bin/env python3
"""Build a compact, disposable heading-level Markdown retrieval index."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

EXCLUDED_PARTS = {
    ".git", ".cache", ".next", ".venv", "__pycache__", "build", "dist",
    "node_modules", "z_archive", "z_temp",
}
INDEX_NAME = "MEMORY_READ_INDEX.json"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def excluded(path: Path) -> bool:
    return any(part.lower() in EXCLUDED_PARTS for part in path.parts) or path.name == INDEX_NAME


def sections(text: str) -> list[tuple[str, str]]:
    heading = "Document"
    body: list[str] = []
    result: list[tuple[str, str]] = []
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            chunk = "\n".join(body).strip()
            if chunk:
                result.append((heading, chunk))
            heading, body = match.group(1).strip(), []
        else:
            body.append(line)
    chunk = "\n".join(body).strip()
    if chunk:
        result.append((heading, chunk))
    return result


def iter_markdown(root: Path, includes: list[Path]):
    seen: set[Path] = set()
    for target in includes:
        candidates = [target] if target.is_file() else target.rglob("*.md") if target.exists() else []
        for path in candidates:
            path = path.resolve()
            try:
                relative = path.relative_to(root)
            except ValueError:
                continue
            if path in seen or excluded(relative):
                continue
            seen.add(path)
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include", action="append", default=[], help="Repository-relative file or folder; repeatable")
    parser.add_argument("--output", help="Repository-relative output path")
    args = parser.parse_args()

    root = repo_root()
    include_names = args.include or ["Operator Team OS/6. Memory", "Operator Team OS/WIKI.md"]
    includes = [(root / name).resolve() for name in include_names]
    for target in includes:
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise SystemExit(f"Refusing path outside repository: {target}") from exc

    output = (root / args.output).resolve() if args.output else root / "Operator Team OS/6. Memory" / INDEX_NAME
    try:
        output.relative_to(root)
    except ValueError as exc:
        raise SystemExit(f"Refusing output outside repository: {output}") from exc
    output.parent.mkdir(parents=True, exist_ok=True)
    records = []
    source_hash = hashlib.sha256()
    for path in sorted(iter_markdown(root, includes)):
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(root).as_posix()
        source_hash.update(relative.encode())
        source_hash.update(text.encode())
        for heading, body in sections(text):
            plain = re.sub(r"\s+", " ", body).strip()
            records.append({
                "path": relative,
                "heading": heading,
                "text": plain[:1600],
            })

    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "includes": include_names,
        "source_hash": source_hash.hexdigest(),
        "records": records,
    }
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Indexed {len(records)} sections from {len({r['path'] for r in records})} files")
    print(output.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
