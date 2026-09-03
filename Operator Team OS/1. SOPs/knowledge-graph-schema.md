---
type: sop
title: Knowledge Graph Schema
owner: shared
status: active
last-reviewed: 2026-09-03
tags: [type/sop, status/active, domain/operations]
---

# Knowledge Graph Schema

This is the authoritative metadata and linking schema for active Markdown in the
Operator OS and any opted-in `Drive - *` knowledge library.

## Exclusions

Do not ingest or index dependencies, caches, build output, generated indexes,
`z_temp/`, or archive folders. Matching is case-insensitive.

## Required frontmatter

| Type | Required fields |
|:---|:---|
| `reference`, `strategy`, `research`, `playbook`, `contract` | `type`, `domain`, `last-updated`, `author`, `tags` |
| `sop` | `type`, `title`, `owner`, `status`, `last-reviewed`, `tags` |
| `agent` | `type`, `title`, `domain`, `status`, `tags` |
| `workflow` | `type`, `triggers`, `requires`, `status`, `tags`, `description` |
| `plan` | `type`, `status`, `owner`, `created`, `tags` |
| `memory`, tier `active` or `long-term` | `type`, `tier`, `last-reviewed`, `tags` |
| `memory`, tier `log` | `type`, `tier`, `date`, `tags` |

Use `human`, `llm`, or `mixed` for `author`. Use `active`, `draft`, `blocked`,
`complete`, or `deprecated` for ordinary status values.

## Starter taxonomy

- Type: `type/sop`, `type/agent`, `type/skill`, `type/workflow`, `type/plan`,
  `type/memory`, `type/reference`, `type/research`, `type/playbook`, `type/strategy`
- Status: `status/active`, `status/draft`, `status/blocked`, `status/complete`,
  `status/deprecated`
- Priority: `priority/p0`, `priority/p1`, `priority/p2`
- Memory: `tier/log`, `tier/active`, `tier/long-term`
- Domain: `domain/operations`, `domain/product`, `domain/marketing`,
  `domain/sales`, `domain/finance`, `domain/legal`, `domain/people`, `domain/it`

Extend the taxonomy here before treating a new tag family as canonical. A tag
used once is a review signal, not automatically an error.

## Link conventions

- Use a relative Markdown link when the path matters or crosses libraries.
- Use wiki-link syntax for an unambiguous filename in the same permitted scope.
- Use display text when a filename is not reader-friendly.
- A unique skill folder link such as `memory-read` resolves to that folder's
  `SKILL.md`; workflow and SOP names resolve to their Markdown files.
- Never create shared `file://` links or named home-directory paths.
- Do not make a folder index for every directory. Use `WIKI.md`, natural folders,
  metadata, and explicit links.

## Derived navigation

Generated indexes may derive headings, aliases, and explicit links for retrieval,
but they remain disposable caches. They must not invent facts or relationships.
Conflicting definitions stay separate until a human resolves them.

## Frontmatter changes

Merge missing fields without discarding existing metadata. If an active file
needs a new type or tag family, update this schema first.
