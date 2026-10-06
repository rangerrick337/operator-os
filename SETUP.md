# Setup Guide

## 1. Clone and check the workspace

```bash
git clone https://github.com/rangerrick337/operator-os.git
cd operator-os
python3 "Operator Team OS/3. Skills/workspace-doctor/scripts/operator_doctor.py"
```

Python 3.10+ is sufficient for the core memory and doctor scripts; they use only
the standard library. Bundled artifact skills may have additional requirements.

## 2. Customize without breaking the architecture

1. Read `Operator Team OS/AGENTS.md` and `Operator Team OS/WIKI.md`.
2. Replace placeholders in `6. Memory/ACTIVE.md` and `LONG_TERM.md`.
3. Keep durable facts out of Long-Term until a human confirms them.
4. Add your own approved domain tags to `1. SOPs/knowledge-graph-schema.md`.
5. Copy `Drive - Example/` to a clearly named knowledge library such as
   `Drive - Operations/`. Keep restricted libraries separate.
6. Add SOPs, skills, and workflows only when the responsibility belongs there.

## 3. Use memory retrieval

```bash
python3 "Operator Team OS/3. Skills/memory-read/scripts/build_index.py"
python3 "Operator Team OS/3. Skills/memory-read/scripts/query.py" \
  --query "current priorities"
```

To include a knowledge library, pass it explicitly with `--include`. Do not put
libraries with different permissions into the same index.

## 4. Save a session handoff

```bash
python3 "Operator Team OS/3. Skills/memory-manage/scripts/append_session_log.py" \
  --topics "Operations planning" \
  --decision "Use one canonical SOP" \
  --action "Owner to validate the rollout" \
  --verification "Workspace doctor passed"
```

Logs are concise handoffs, not transcripts. Rebuild the memory index afterward.

## 5. Connect an AI platform

Cursor, Codex, Claude Code, and Antigravity read the root `AGENTS.md` natively. It is
an ordinary pointer file so it survives OneDrive, Dropbox, and SharePoint sync.
Do not add a `CLAUDE.md`: Claude Code reads `AGENTS.md` only when no `CLAUDE.md`
exists. Gemini CLI reads `GEMINI.md` by default; to use `AGENTS.md` instead, add
`{ "context": { "fileName": "AGENTS.md" } }` to your own `.gemini/settings.json`.
If another platform needs a special directory, add a small wrapper that routes to
canonical content; do not copy policy into a second source of truth.

## 6. Secrets and integrations

Copy `.env.example` to `.env` and store local values there. Never commit secrets.
Treat `.agent/mcp_config.json` as a structural example only; use environment
variables or your platform's secret store for credentials. External actions such
as sending, publishing, spending, deployment, or recurrence need explicit human
authorization.

## 7. Validate changes

After structural edits:

```bash
python3 "Operator Team OS/3. Skills/workspace-doctor/scripts/operator_doctor.py"
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
git status --short
```

Review the diff before committing or pushing.
