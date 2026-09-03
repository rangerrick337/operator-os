---
name: memory-read
description: Query-first indexing and retrieval for Operator OS memory. Use when asked to find prior context, search memory, rebuild the memory index, or answer from the workspace without loading large files by default.
allowed-tools: [read_file, list_directory, shell]
---

# Memory Read

Build an explicit local index, query it, then open only the returned source
section. This keeps context small and answers traceable.

## Retrieval protocol

1. Run `scripts/query.py --query "..."` against the generated index.
2. Never read the complete index, `ACTIVE.md`, `LONG_TERM.md`, or all logs into
   model context by default.
3. Open the highest-scoring source section. Follow at most one useful explicit
   link unless the user asks for a deep dive.
4. Return the path, heading, and a concise evidence-based answer.
5. If there is no positive match, refine the query; do not present a fallback as
   evidence.

## Commands

Run from the repository root:

```bash
python3 "Operator Team OS/3. Skills/memory-read/scripts/build_index.py"
python3 "Operator Team OS/3. Skills/memory-read/scripts/query.py" --query "current priorities"
```

The default scope is `Operator Team OS/6. Memory/` plus `Operator Team OS/WIKI.md`.
Add a permitted knowledge library explicitly with repeated `--include` arguments:

```bash
python3 "Operator Team OS/3. Skills/memory-read/scripts/build_index.py" \
  --include "Operator Team OS/6. Memory" --include "Drive - Example"
```

Never combine libraries with different permissions into one index. The generated
`MEMORY_READ_INDEX.json` file is a disposable local cache and must not be treated
as a source of truth or committed.

Memory writes belong to [[memory-manage]]. Rebuild the index after a write.
