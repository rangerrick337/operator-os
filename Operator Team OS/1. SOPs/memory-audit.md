---
type: sop
title: Memory Audit
owner: shared
status: active
last-reviewed: 2026-09-03
tags: [type/sop, status/active, type/memory, domain/operations]
---

# Memory Audit

Produce a punch list; do not auto-fix findings.

Check active Markdown for:

1. Missing frontmatter required by [[knowledge-graph-schema]].
2. Empty tags or tags outside the approved taxonomy.
3. Broken wiki-links and relative Markdown links.
4. Stale review dates and overdue active plans.
5. Cloud-sync conflict filenames and duplicate copies.
6. References that cross a permission boundary.
7. `file://` links, named home directories, or other machine-local paths.
8. Secrets or credential-shaped content in shared files.

Write dated reports to `6. Memory/lint/`. Include files scanned, issue counts,
paths and lines, impact, and recommended owner. The user decides what to fix.
