# Agent Instructions

> **⚠️ CORE FRAMEWORK DOCUMENTATION**
>
> This file contains the canonical instructions for the 5-Layer Operator OS.
> It defines the architecture, operating principles, and file organization for AI agent systems.

You operate within a 5-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

## The 5-Layer Architecture


**Layer 1: SOPs (What to do)**

- Written in Markdown, live in `Operator Team OS/1. SOPs/`
- Human-readable process documentation
- Define goals, context, inputs, outputs, and edge cases
- Natural language instructions, like you'd give a mid-level employee

**Layer 2: Agents (Who to be)**

- Specialized personas in `Operator Team OS/2. Agents/`
- Define voice, expertise, model preference, and decision-making style
- Activated when specific persona/expertise is needed

**Layer 2a: The Activation Pattern (How to "Be" an Agent)**
To create a switchable persona:
1.  **Define (`Operator Team OS/2. Agents/MyAgent.md`)**: The "Resume" (Voice, Model, Tools).
2.  **Trigger (`Operator Team OS/4. Workflows/be-my-agent.md`)**: The "Job Order".
    - Content: "You are now [Agent Name]. Read `Operator Team OS/2. Agents/MyAgent.md` and adopt persona."
3.  **Sync**: Run `workflow-sync` to make the slash command available.


**Layer 3: Skills (How to execute)**

- Anthropic-format skills in `Operator Team OS/3. Skills/`
- Each skill has `SKILL.md` (instructions + YAML frontmatter) + `scripts/` (code)

- **Progressive disclosure**: Read YAML frontmatter first, load full instructions only when needed
- Scripts are deterministic Python—reliable, testable, fast

**Layer 4: Workflows (Sequences)**

- Live in `Operator Team OS/4. Workflows/` (Canonical Source)
- Symlinked to `.agent/workflows` for Antigravity compatibility (allows `/` slash commands)
- Sequential "fire and forget" instructions for repetitive technical tasks
- If Antigravity is used, supports `// turbo` mode for auto-execution

**Layer 5: Knowledge Base (Where data lives)**

- `Drive - [YourProject]/` (Unstructured Data)
- **Distinction**:
    - **SOPs** tell you *how* to do it.
    - **Drive** is where you *put* the result or read the background info.
- **Example**: `Drive - ProjectX/Data/list.csv`

**Why this works:** if you do everything yourself, errors compound. The solution is push complexity into deterministic code and clear instructions.

## Skill Discovery

When user requests a task:

1. **Scan `Operator Team OS/3. Skills/`** for matching skill folders
2. **Read YAML frontmatter** in `SKILL.md` to check relevance (description field)
3. **Load full skill** only if relevant—keeps context lean
4. **Execute scripts** in `scripts/` subfolder as directed by SKILL.md

Example skill structure:
```
Operator Team OS/3. Skills/
├── data-processing/      # Domain-specific skill
│   ├── SKILL.md          # YAML frontmatter + detailed instructions
│   └── scripts/          # Python scripts for this skill
│       ├── process_data.py
│       └── ...
```

## MCP Integration (Model Context Protocol)

MCP servers provide the raw connections to external tools (GitHub, Database, etc.). They sit *below* the Skills layer.

**1. Installation (The "Single Source")**
- **Master Config**: `.agent/mcp_config.json`
- **Sync**: This file defines which MCP servers are available to your agents.

**2. How to Add a Tool**
- Open `.agent/mcp_config.json`.
- Add the server definition under `"mcpServers"` (e.g., `github`, `postgres`).
- Your AI platform will auto-detect the new server.

**3. Access Control (The Permission Gate)**
- **Availability**: Adding it to the config makes it *technically* available.
- **Permission**: An Agent will **only** use the tool if you explicitly list it in their persona file (`Operator Team OS/2. Agents/*.md`) under the `tools:` key.
- **Protocol**: Never give an Agent "all tools". Only license them for what they need.

**4. Best Practice: Dual Listing**
Since we use both Agents and Skills, list tools in **both** places:
1.  **In `Operator Team OS/2. Agents/*.md`**: Grants the *Permission* for the agent to use it.
2.  **In `Operator Team OS/3. Skills/*/SKILL.md`**: Adds `allowed-tools: [tool_name]` to the frontmatter. This helps the Orchestrator know *what capabilities a skill requires*.

## Operating Principles

**1. Check for skills first**
Before writing a script, check `Operator Team OS/3. Skills/` for an existing skill. Only create new skills/scripts if none exist.

**2. Self-anneal when things break**

- Read error message and stack trace
- Fix the script and test it again (unless it uses paid tokens/credits—check with user first)
- Update the skill's SKILL.md with what you learned (API limits, timing, edge cases)
- Example: you hit an API rate limit → investigate → find a batch endpoint → rewrite script → test → update SKILL.md

**3. Update skills and SOPs as you learn**
These are living documents. When you discover API constraints, better approaches, common errors, or timing expectations—update them. But don't create or overwrite without asking unless explicitly told to.

## Response Mode Selection

Before taking action, assess what the user actually needs:

**1. Conversational (no tools needed)**
- General advice, opinions, explanations, brainstorming
- Questions you can answer from training knowledge
- Clarifying questions back to the user
- *Default to this unless there's a clear reason to use tools*

**2. Research (web/external tools)**
- Current events, recent updates, "what's the latest on X?"
- External API documentation, third-party service info
- Market research, competitor info, general lookups
- Use `search_web` for quick answers, `read_url_content` for deep dives

**3. Codebase exploration (file/code tools)**
- "What do we have for X?" or "How does Y work in our system?"
- Debugging existing code, understanding current implementation
- Use `grep_search`, `find_by_name`, `view_file`, etc.

**4. Execution (writing/modifying code)**
- Explicit requests to build, fix, create, or modify something
- Only after understanding requirements—don't jump straight here

**When in doubt:** Start conversational. Ask clarifying questions. You can always escalate to tools, but you can't un-ring the bell of diving into an implementation the user didn't want.

## Self-annealing loop

Errors are learning opportunities. When something breaks:

1. Fix it
2. Update the script
3. Test script, make sure it works
4. Update SKILL.md to include new flow
5. System is now stronger

## File Organization

**Deliverables vs Intermediates:**

- **Deliverables**: Cloud-based outputs (OneDrive, SharePoint, etc.) that the user can access
- **Intermediates**: Temporary files needed during processing

**Directory structure:**

- `Operator Team OS/z_temp/` - **MANDATORY** for all one-off processing, intermediate files, and temporary automation scripts (e.g., `checkfiles.py`, `pdf_list.txt`). These files must never be created in the root or major project folders.
- `Operator Team OS/1. SOPs/` - Human-readable process docs (the instruction set)
- `Operator Team OS/2. Agents/` - Specialized AI personas
- `Operator Team OS/3. Skills/` - Anthropic-format skills with scripts
  - `_shared/` - Utilities used across skills
  - `<skill-name>/` - Individual skill folders
- `Operator Team OS/4. Workflows/` - Sequential execution plans
- `Drive - *` - Long-term storage (e.g., `Drive - ProjectX`)
- `.env` - Environment variables and API keys
- `credentials.json`, `token.json` - OAuth credentials (add to `.gitignore`)

**Key principle:** Local files are only for processing. Deliverables live in cloud services where the user can access them. Everything in `Operator Team OS/z_temp/` is ephemeral and should be deleted once the task is complete.

**Verification Protocol (Post-Operation):**
**MANDATORY**: After any file deletion, move, or bulk rename operation, you must perform a verification check:
1.  **Confirmation**: Use `ls` or `find` to confirm the intended files are no longer in the source location (for deletions) or are correctly placed in the destination (for moves).
2.  **Safety Scan**: Perform a quick scan of the parent directory to ensure critical configuration files (e.g., `.gitignore`, `.env`, `AGENTS.md`) weren't accidentally caught in a wildcard or recursive operation.
3.  **Git Audit**: If working in a version-controlled folder, run `git status` immediately after the operation. You **MUST** review the list of "deleted" or "modified" files to verify that only the expected items were affected before proceeding.
4.  **Reporting**: Explicitly state to the user that you have verified the operation was clean and no side-effects occurred.

**Tool Permissions (Soft Gating):**
- The `tools:` list in an Agent definition (`SKILL.md` or `Agents/*.md`) acts as a **Strict Instruction**.
- If a tool is NOT listed, you must pretend you cannot use it.
- **Example**: If `ResearchAgent.md` does not list `write_file`, you must refuse to write code.
- **Exception**: You may always use "Read Only" tools (`view_file`, `ls`) to understand context unless explicitly forbidden.


**Cross-Platform Compatibility:**
We support multiple AI agents (Antigravity, Claude Code, OpenDevin, Cursor, etc.) using a "Single Source of Truth" strategy:
- **Canonical Files**: All instructions and workflows live in top-level folders (`Operator Team OS/1. SOPs/`, `Operator Team OS/2. Agents/`, `Operator Team OS/4. Workflows/`, `AGENTS.md`).
- **Platform-Specific folders**: If a platform requires a specific folder structure (e.g., `.agent/workflows`, `.cursorrules`), create a **symlink** pointing to the canonical location.
- **Do NOT duplicate files**: Never copy files to platform folders. Always symlink.


**Dynamic Path Resolution:**
When writing scripts that access the `Drive` folder, avoid hardcoding paths if possible, or use a configurable environment variable.



## Summary

You sit between human intent (SOPs, user requests) and deterministic execution (Python scripts in Skills). Read instructions, make decisions, call skills, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.
