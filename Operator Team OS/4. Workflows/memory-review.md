---
type: workflow
triggers: [/memory-review]
requires: [memory-manage, memory-read]
status: active
tags: [type/workflow, status/active, type/memory]
description: Review stale Active context and proposed Long-Term updates.
---

# Memory Review

1. Query for current priorities, blockers, decisions, and pending proposals.
2. Review relevant Active sections and recent handoffs; do not load every log.
3. Present Long-Term proposals with source and rationale for approve, revise, or
   reject decisions.
4. Apply only confirmed promotions, prune Active only with evidence, and preserve
   the proposal decision trail.
5. Rebuild the index and summarize changes and unresolved items.
