---
type: workflow
triggers: [/memory-save]
requires: [memory-manage]
status: active
tags: [type/workflow, status/active, type/memory]
description: Save a confirmed Active update, session handoff, or Long-Term proposal.
---

# Memory Save

1. Load [[memory-manage]] and query existing memory first.
2. Classify the item as Active, session log, or Long-Term proposal.
3. Write Active only from confirmed evidence; use the session helper for logs.
4. Stage Long-Term candidates in `6. Memory/proposals/` and require explicit human
   approval before promotion.
5. Rebuild the memory index and report the exact file changed.
