# Operator OS

> A portable six-layer operating system for reliable AI-assisted business work.

Operator OS gives humans and AI agents one shared, inspectable structure for
process, execution, knowledge, and memory. It is based on an operating system
used in a real business, generalized here without company data or private rules.

## Why it exists

LLMs are probabilistic; many business processes require consistency. Operator OS
separates judgment from repeatable execution so teams do not have to re-explain
their standards every session or bury every rule in one enormous prompt.

## The six layers

| Layer | Purpose | Location |
|:---|:---|:---|
| 1. SOPs | Durable process and governance | `Operator Team OS/1. SOPs/` |
| 2. Agents | Optional specialist roles | `Operator Team OS/2. Agents/` |
| 3. Skills | Task instructions and deterministic tools | `Operator Team OS/3. Skills/` |
| 4. Workflows | Short routers and repeatable sequences | `Operator Team OS/4. Workflows/` |
| 5. Knowledge | Permissioned business data | `Drive - *` folders |
| 6. Memory | Active context, durable facts, session handoffs | `Operator Team OS/6. Memory/` |

The numbered `5. Implementation Plans/` folder tracks approved changes to the OS;
business knowledge stays outside the OS container so permissions remain clear.

## What is new in 2.0

- One canonical policy file with portable, non-symlink discovery pointers
- Query-first memory retrieval instead of loading whole memory files
- Atomic session handoffs instead of shared daily-log appends
- Human approval before durable facts enter Long-Term memory
- A knowledge-graph schema, master WIKI, and audit/intake workflows
- A read-only workspace doctor and lightweight context-audit skill
- Stronger privacy, secret, dependency, cache, and cloud-sync hygiene

## Quick start

```bash
git clone https://github.com/rangerrick337/operator-os.git
cd operator-os
python3 "Operator Team OS/3. Skills/workspace-doctor/scripts/operator_doctor.py"
```

Then ask your AI tool: “Read `AGENTS.md` and help me customize Operator OS.”

Useful entrypoints:

- `Operator Team OS/WIKI.md` — map of the system
- `/start` — begin with compact context
- `/memory` — retrieve, save, review, intake, or audit context
- `/wrap-up` — surface confidence gaps and blind spots
- `SETUP.md` — customize the template safely

## Included skills

- `memory-read` — heading-level, source-linked local retrieval
- `memory-manage` — Active updates, proposals, and session handoffs
- `workspace-doctor` — read-only structural and portability checks
- `ai-context-optimizer` — detect duplicated or stale AI-facing context
- `wrap-up` — end-of-session uncertainty and blind-spot review
- Document, presentation, spreadsheet, and conversion examples from the original
  public release remain available for teams that need artifact workflows.

## Design principles

- One canonical source; small platform pointers
- Progressive disclosure; load only what the task needs
- Deterministic scripts for repeatable mechanics
- Explicit permission boundaries for knowledge and memory
- Evidence before synthesis; human approval at consequential write boundaries
- Reversible maintenance and inspectable Markdown

Operator OS is platform-agnostic. Different tools may need small discovery
wrappers, but canonical policy, skills, and workflows stay under `Operator Team OS/`.

## License

MIT. See `LICENSE` and retain any additional license files shipped with bundled
third-party skills.
