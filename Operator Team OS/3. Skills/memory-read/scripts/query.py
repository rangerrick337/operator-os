#!/usr/bin/env python3
"""Query the local Operator OS memory index without loading it into an agent."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def tokens(value: str) -> list[str]:
    return re.findall(r"[a-z0-9][a-z0-9_-]+", value.lower())


def score(record: dict, terms: list[str]) -> int:
    heading = record["heading"].lower()
    path = record["path"].lower()
    text = record["text"].lower()
    return sum((5 if term in heading else 0) + (3 if term in path else 0) + text.count(term) for term in terms)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--max-results", type=int, default=5)
    parser.add_argument("--index", default="Operator Team OS/6. Memory/MEMORY_READ_INDEX.json")
    args = parser.parse_args()
    if args.max_results < 1:
        raise SystemExit("--max-results must be positive")

    root = Path(__file__).resolve().parents[4]
    index = (root / args.index).resolve()
    try:
        index.relative_to(root)
    except ValueError as exc:
        raise SystemExit(f"Refusing index outside repository: {index}") from exc
    if not index.exists():
        raise SystemExit("Memory index missing. Run build_index.py first.")
    terms = tokens(args.query)
    if not terms:
        raise SystemExit("Query has no searchable terms")

    payload = json.loads(index.read_text(encoding="utf-8"))
    ranked = sorted(
        ((score(record, terms), record) for record in payload.get("records", [])),
        key=lambda item: (-item[0], item[1]["path"], item[1]["heading"]),
    )
    results = []
    for value, record in ranked:
        if value <= 0 or len(results) >= args.max_results:
            break
        results.append({
            "score": value,
            "path": record["path"],
            "heading": record["heading"],
            "excerpt": record["text"][:360],
        })
    print(json.dumps({"query": args.query, "results": results}, indent=2))
    return 0 if results else 2


if __name__ == "__main__":
    raise SystemExit(main())
