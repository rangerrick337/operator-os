#!/usr/bin/env python3
"""Create one immutable, concise session handoff file."""

from __future__ import annotations

import argparse
import re
import secrets
from datetime import datetime
from pathlib import Path


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def bullets(title: str, values: list[str]) -> str:
    if not values:
        return ""
    return f"\n## {title}\n\n" + "\n".join(f"- {clean(v)}" for v in values) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topics", required=True)
    parser.add_argument("--decision", action="append", default=[])
    parser.add_argument("--action", action="append", default=[])
    parser.add_argument("--verification", action="append", default=[])
    parser.add_argument("--source", action="append", default=[])
    args = parser.parse_args()

    fields = [args.topics, *args.decision, *args.action, *args.verification, *args.source]
    word_count = len(" ".join(fields).split())
    if word_count > 220:
        raise SystemExit(f"Session handoff is {word_count} words; keep it at or below 220")

    now = datetime.now().astimezone()
    root = Path(__file__).resolve().parents[4]
    log_dir = root / "Operator Team OS/6. Memory/logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{now:%Y-%m-%d_%H%M%S}_{secrets.token_hex(3)}.md"
    path = log_dir / filename
    content = (
        "---\n"
        "type: memory\n"
        "tier: log\n"
        f"date: {now:%Y-%m-%d}\n"
        "author: mixed\n"
        "tags: [type/memory, tier/log]\n"
        "---\n\n"
        f"# Session Handoff — {now:%Y-%m-%d %H:%M %Z}\n\n"
        f"**Topics:** {clean(args.topics)}\n"
        + bullets("Decisions", args.decision)
        + bullets("Next actions", args.action)
        + bullets("Verification", args.verification)
        + bullets("Sources", args.source)
    )
    with path.open("x", encoding="utf-8") as handle:
        handle.write(content)
    print(path.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
