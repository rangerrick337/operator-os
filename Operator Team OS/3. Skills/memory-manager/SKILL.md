---
name: memory-manager
description: "Manages the 3-tier memory system. Use when: (1) the user says 'remember this' or 'commit to memory', (2) a significant decision or fact is established, (3) the user runs /memory-save or /memory-review, (4) at session start to load memory context, or (5) at session end to flush important context to logs."
---

# Memory Manager Skill

## Memory Location

All memory files live in `Operator Team OS/6. Memory/`.

## 3-Tier System

| Tier | File | Purpose | Who Writes |
|:---|:---|:---|:---|
| **Long-Term** | `LONG_TERM.md` | Canonical company facts. Rarely changes. | Agent proposes, human confirms |
| **Active** | `ACTIVE.md` | Company dashboard — who's working on what, links to real files. | Agent writes, human reviews |
| **Logs** | `logs/YYYY-MM-DD.md` | Daily session summaries. Append-only. | Agent auto-generates |

## Reading Memory (Session Start)

Load in this order:
1. `6. Memory/LONG_TERM.md` (always)
2. `6. Memory/ACTIVE.md` (always)
3. `6. Memory/logs/` — today's file and yesterday's file if they exist

## Writing Memory

### Long-Term (`LONG_TERM.md`)
- **Never write directly.** Propose changes to the user.
- Format: append `[PROPOSED YYYY-MM-DD] <fact>` and ask user to confirm.

### Active (`ACTIVE.md`)
- Write directly when priorities shift or a significant decision is made.
- Date-stamp entries in the "Recent Decisions" section.
- Update per-person "Focus" and "Where We're At" sections.
- **Link to deeper files** using relative paths.
- Active is a **map**, not a warehouse. Keep it brief and point to the real work.

### Logs (`logs/YYYY-MM-DD.md`)
- **One file per day, shared across all users.** 
- Append session summaries at end of session, or when context is about to be lost.
- Format:

```
## Session — HH:MM (User Name)

**Topics**: topic1, topic2
**Decisions**:
- Decision description and rationale

**Action Items**:
- [ ] Action item description

**Notes**:
- Any other noteworthy context
```

## Proactive Memory Behavior

When a conversation surfaces a significant decision, preference, or factual change:
1. Assess if it's worth remembering (not trivial details)
2. Offer: "This seems important — want me to commit it to memory?"
3. If yes, write to the appropriate tier
4. If unsure which tier, default to Active

Do NOT ask about trivial or obvious things. Use judgment.
