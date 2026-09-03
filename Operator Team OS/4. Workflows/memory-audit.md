---
type: workflow
triggers: [/memory-audit]
requires: [memory-audit]
status: active
tags: [type/workflow, status/active, type/memory]
description: Produce a read-only knowledge and memory health punch list.
---

# Memory Audit Workflow

Read `1. SOPs/memory-audit.md` and `1. SOPs/knowledge-graph-schema.md`. Audit the
requested scope, write a dated report to `6. Memory/lint/`, and summarize findings.
Do not fix findings without authorization.
