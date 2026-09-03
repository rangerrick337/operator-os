# Operator OS Agent Instructions

> This is the single source of truth for the workspace. Root and platform files
> are small discovery pointers. Keep policy here rather than maintaining copies.

## Workspace contract

- Start at the repository root and use repository-relative paths in shared files.
- Never write a user name, home directory, secret, token, or machine-specific
  cloud-storage path into shared content.
- Keep the operating system in `Operator Team OS/` and business knowledge in one
  or more separately permissioned `Drive - *` folders.
- Put one-off probes and intermediates in `Operator Team OS/z_temp/`; keep only
  intentional source and deliverables elsewhere.
- Preserve user-owned edits. Do not run destructive resets or publish external
  changes without explicit authorization.

## Six-layer operating model

1. **SOPs — what to do:** durable human-readable process and governance.
2. **Agents — who to be:** optional specialist roles and decision styles.
3. **Skills — how to execute:** task-specific instructions and deterministic tools.
4. **Workflows — sequence:** short entrypoints that route to SOPs and skills.
5. **Knowledge — business data:** `Drive - *` libraries, separated by permissions.
6. **Memory — current context:** durable facts, an active dashboard, and session logs.

`5. Implementation Plans/` is an OS workspace for approved changes. It is not a
substitute for the Knowledge layer, which remains outside the OS container.

Keep concerns in their layer. A workflow routes, a skill executes, an SOP owns
durable process, and memory records current context. Avoid repeating policy.

## Task routing

1. Determine whether the user wants an answer, diagnosis, research, or a change.
2. Check the available skill catalog and read a complete `SKILL.md` only when its
   description matches the task.
3. Read only the necessary SOP, source section, or reference.
4. Prefer an existing tested script over one-off automation.
5. Keep work outcome-first; write code only when implementation requires it.
6. Verify in proportion to risk and report evidence and unresolved risk.

Default to one agent. Delegate only when the user requests it, and give each
delegate a bounded outcome. The primary agent owns synthesis and final delivery.

## Memory and context

- Use `memory-read` as the default retrieval layer. Query its generated index;
  do not inject the complete index, `ACTIVE.md`, `LONG_TERM.md`, or all logs into
  model context by default.
- Open the best matching source section first and follow at most one useful link.
- `LONG_TERM.md` contains confirmed durable facts. Stage candidates in
  `6. Memory/proposals/` and require human confirmation before promotion.
- `ACTIVE.md` is a concise dashboard of current focus, blockers, next actions,
  and links—not a history warehouse.
- Logs are short, immutable, per-session handoffs. Do not append every exchange.
- After a memory change, rebuild the memory index.
- At the end of meaningful work, `/wrap-up` can surface confidence gaps and blind
  spots. It is reflection, not approval.

The authoritative metadata, taxonomy, and link rules live in
`1. SOPs/knowledge-graph-schema.md`.

## Knowledge and privacy boundaries

- Treat each `Drive - *` library as an independent permission boundary.
- Retrieval and summaries must not expose a more restricted library into a less
  restricted one merely because the current machine can access both.
- Never log credentials, cookies, personal data that is not necessary, private
  keys, or raw authentication material.
- Generated indexes are disposable routing caches, never knowledge authorities.

## File hygiene

- Exclude `z_temp/`, archive folders, dependencies, caches, build output, and
  generated indexes from normal knowledge retrieval unless explicitly requested.
- Do not store virtual environments, `node_modules`, `.next`, `.cache`, `dist`,
  `build`, or `__pycache__` in a synced workspace.
- New plan filenames use `YYYY-MM-DD_<slug>.md` with matching `created:` metadata.
- Move completed or superseded plans to `5. Implementation Plans/z_archive/`.
- Prefer plain pointer files over symlinks in cloud-synced workspaces.

After a deletion, move, or bulk rename: verify source and destination, scan the
parent for unintended effects, inspect Git status, and report remaining review.

## Change and safety rules

- Read, audit, and diagnose without changing source unless a change was requested.
- When a change is requested, implement within scope and verify the outcome.
- Preserve legal, financial, security, architecture, and deployment records.
- Prefer reversible archive moves over deletion for business records.
- Do not spend, send, publish, deploy, alter production, or create recurring
  automation without explicit authorization.
- Keep secrets in local configuration. Shared files may document variable names,
  never secret values.

## Platform discovery

Keep canonical content in `Operator Team OS/`. Platform-specific folders may
contain small generated pointers or wrappers, but never independent policy.
Regenerate wrappers when canonical skills or workflows change. Tool declarations
describe capabilities; shared instructions must not depend on one vendor's tool
names or model roster.

## Definition of done

- Confirm the requested deliverable or result.
- Run relevant tests and inspect the final Git diff/status.
- State checks performed and unresolved risks.
- Update plans, SOPs, skills, or memory only when the work materially changed that
  system and the write is authorized.
