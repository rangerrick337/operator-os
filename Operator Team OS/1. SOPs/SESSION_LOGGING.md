---
type: sop
title: Session Logging
owner: shared
status: active
last-reviewed: 2026-09-03
tags: [type/sop, status/active, type/memory, domain/operations]
---

# Session Logging

Create a log only when a session produced a durable decision, meaningful state
change, blocker, or handoff. A log is not a transcript.

## Contract

- One immutable Markdown file per session in `6. Memory/logs/`.
- Use `memory-manage/scripts/append_session_log.py`; do not append to a shared
  daily file.
- Keep the summary concise—normally under 180 words.
- Record topics, decisions, next actions, verification, and source links.
- Never store secrets, raw credentials, sensitive personal data, or information
  from a more restricted knowledge library.
- Rebuild the memory index after writing.

If the session reveals a durable fact, stage a proposal rather than modifying
`LONG_TERM.md` without human confirmation.
