#!/usr/bin/env python3
"""Generate deterministic Operator OS release metadata."""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    os_root = root / "Operator Team OS"
    source_files = [os_root / "AGENTS.md", os_root / "VERSION"]
    source_files += sorted((os_root / "2. Agents").glob("*.md"))
    source_files += sorted((os_root / "3. Skills").glob("*/SKILL.md"))
    source_files += sorted((os_root / "4. Workflows").glob("*.md"))
    digest = hashlib.sha256()
    for path in source_files:
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode())
        digest.update(path.read_bytes())
    payload = {
        "schema_version": 1,
        "os_name": "Operator OS",
        "os_version": (os_root / "VERSION").read_text().strip(),
        "generated_on": date.today().isoformat(),
        "source_hash_algorithm": "sha256",
        "source_hash": digest.hexdigest(),
        "source_scope": [
            "Operator Team OS/AGENTS.md",
            "Operator Team OS/VERSION",
            "Operator Team OS/2. Agents/*.md",
            "Operator Team OS/3. Skills/*/SKILL.md",
            "Operator Team OS/4. Workflows/*.md",
        ],
        "counts": {
            "agents": len(list((os_root / "2. Agents").glob("*.md"))),
            "skills": len(list((os_root / "3. Skills").glob("*/SKILL.md"))),
            "workflows": len(list((os_root / "4. Workflows").glob("*.md"))),
        },
    }
    output = os_root / "MANIFEST.json"
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(output.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
