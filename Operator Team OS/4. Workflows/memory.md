---
type: workflow
triggers: [/memory]
requires: []
status: active
tags: [type/workflow, status/active, type/memory]
description: Primary router for memory retrieval, saves, intake, review, and audit.
---

# Memory Router

| Intent | Route |
|:---|:---|
| Find prior context | Load [[memory-read]] and query first |
| Save a decision or handoff | [[memory-save]] |
| Add a file or folder | [[4. Workflows/memory-intake|memory intake]] |
| Review proposals and stale context | [[memory-review]] |
| Audit metadata, links, privacy, or staleness | [[4. Workflows/memory-audit|memory audit]] |

Do not load complete indexes or logs by default. Preserve library permission
boundaries before retrieval or writing.
