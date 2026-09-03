---
name: memory-manage
description: Manage Active updates, atomic session handoffs, and human-gated Long-Term proposals. Use when asked to remember something, preserve a decision, log meaningful work, or review memory.
---

# Memory Management

| Tier | Location | Purpose | Write policy |
|:---|:---|:---|:---|
| Long-Term | `6. Memory/LONG_TERM.md` | Confirmed durable facts | Human confirmation required |
| Active | `6. Memory/ACTIVE.md` | Focus, blockers, next actions | Update from confirmed evidence |
| Logs | `6. Memory/logs/` | Concise session handoffs | One immutable file per session |

Use [[memory-read]] before writing so new information does not duplicate or
contradict existing memory.

## Long-Term

Stage candidates under `6. Memory/proposals/` with source, rationale, and proposed
wording. Ask a human to approve, revise, or reject them. Only explicit approval
allows promotion into `LONG_TERM.md`.

## Active

Update when confirmed evidence materially changes current priorities, blockers,
or next actions. Keep the dashboard short and link to deeper sources.

## Logs

Follow [[SESSION_LOGGING]] and use:

```bash
python3 "Operator Team OS/3. Skills/memory-manage/scripts/append_session_log.py" \
  --topics "..." --decision "..." --action "..." --verification "..."
```

The helper creates a collision-resistant per-session file. Rebuild the memory
index after any other direct memory change.
