# Operator OS

> A 5-layer architecture for running your business with AI agents

## Background

If you're using AI tools like Claude Code, Cursor, Antigravity, or OpenCode to help run your business, you might have run into some of these issues:

- Re-explaining the same processes to your AI
- Prompts that grow unwieldy and still miss edge cases
- AI that "forgets" how you want things done between sessions
- Scripts and automations scattered with no structure
- Team members using AI inconsistently

I built this framework for my own company. After iterating on it for a while, I figured it might be useful to others dealing with the same challenges.

## What is this?

The Operator OS is a tool-agnostic framework that gives your AI agents a structure they can understand. It can work with Claude Code, Antigravity, OpenCode, Cursor, or whatever comes next. They all read the same files and follow the same instructions.

The core idea: LLMs are probabilistic. Business processes are deterministic. This framework separates those concerns.

## How it helps

**Structure**: Clear separation between instructions, personas, skills, workflows, and data

**Reusability**: Write a process once, use it across sessions and team members

**Self-improvement**: Agents can update documentation when they learn something new

**Platform flexibility**: Not locked into any one AI tool

## The 5 Layers

```
┌─────────────────────────────────────────┐
│  Layer 1: SOPs (What to do)             │  ← Natural language instructions
├─────────────────────────────────────────┤
│  Layer 2: Agents (Who to be)            │  ← Specialized personas
├─────────────────────────────────────────┤
│  Layer 3: Skills (How to execute)       │  ← Deterministic Python scripts
├─────────────────────────────────────────┤
│  Layer 4: Workflows (Sequences)         │  ← Step-by-step automation
├─────────────────────────────────────────┤
│  Layer 5: Knowledge Base (Data)         │  ← Unstructured information
└─────────────────────────────────────────┘
```

### Layer 1: SOPs

Human-readable process documentation. "Here's what needs to happen and why."

### Layer 2: Agents

Specialized personas with defined expertise, voice, and tool permissions. Switch between a Research Agent, Copywriter, or consult your Board of Advisors.

### Layer 3: Skills

Anthropic-format skills with deterministic Python scripts. The AI reads instructions, executes code, handles errors, and self-improves the system.

### Layer 4: Workflows

Sequential "slash command" automations for repetitive tasks. `/consult-board`, `/weekly-review`.

### Layer 5: Knowledge Base

Where your actual data lives. CSVs, documents, API responses.

## Quick Start

### 1. Clone This Repo

```bash
git clone https://github.com/yourusername/operator-os.git
cd operator-os
```

### 2. Choose Your AI Platform

This framework can work with:

- **Claude Code** (Code or API)
- **Antigravity**
- **Open Code**
- **Cursor**
- Any AI that supports file context and tool use

### 3. Read the Docs

Start with `AGENTS.md` to understand the architecture, then explore:

- `1. SOPs/` for example processes
- `2. Agents/` for example persona definitions
- `3. Skills/` for example automation utilities
- `4. Workflows/` for example quick-start commands

### 4. Try It Out

Most AI platforms will automatically read `AGENTS.md` and understand the system. Just start a conversation!

Some included workflows you can try:

- `/consult-board` - Get strategic advice from AI thought leaders
- `/weekly-review` - Summarize progress and plan next steps

## Real-World Examples

### Example 1: Board of Advisors

Consult with simulated versions of Clayton Christensen, Indra Nooyi, Daniel Kahneman, and Steve Jobs for strategic advice.

**Usage**: `/consult-board` → "Should I pivot our product strategy?"

### Example 2: Data Processing

Automated ETL workflows with validation, error handling, and logging.

**Usage**: Agent reads SOP → Finds skill → Executes script → Reports results

### Example 3: Document Generation

Generate branded DOCX, PPTX, or XLSX files.
*(Includes example skills from [Anthropic's skills repository](https://github.com/anthropics/skills))*

**Usage**: Agent calls skill → Populates template → Outputs formatted document

## Key Features

### Progressive Disclosure

Agents only load what they need. YAML frontmatter → Full instructions → Script execution.

### Self-Annealing

When errors occur, the system fixes itself:

1. Agent encounters error
2. Reads stack trace
3. Fixes the script
4. Updates documentation
5. System is now stronger

### Tool Permissions

Fine-grained control over which agents can use which tools. Research Agent gets `search_web`, Data Agent gets `run_command`.

### MCP Integration

Plug in external tools via Model Context Protocol (GitHub, Slack, Databases, etc.)

## Folder Structure

```
operator-os/
├── AGENTS.md              # Core architecture documentation (read this first!)
├── README.md              # This file
├── SETUP.md               # Detailed setup guide
├── .env.example           # API key template
├── .gitignore
│
├── .agent/                # Platform-specific configuration
│   ├── mcp_config.json    # MCP server definitions
│   └── workflows/         # Symlink to 4. Workflows/
│
├── 1. SOPs/               # Standard Operating Procedures
│   └── ...
│
├── 2. Agents/             # Agent persona definitions
│   ├── Board-Strategy.md
│   ├── Board-Risk.md
│   └── ...
│
├── 3. Skills/             # Executable skills with scripts
│   └── ...
│
├── 4. Workflows/          # Sequential automation
│   ├── weekly-review.md
│   └── consult-board.md
│
├── Drive - Example/       # Example data folder
└── z_temp/                # Temporary processing files
```

## Philosophy

### Deterministic > Probabilistic

Push complexity into Python scripts that do one thing reliably. Let AI orchestrate, not execute.

### Living Documentation

SOPs and skills self-improve as agents encounter edge cases and learn better approaches.

### Separation of Concerns

Don't mix "what to do", "who does it", and "how to do it". Each layer has a job.

### Progressive Complexity

Start simple. Add layers only when needed. No premature abstraction.

## Platform-Specific Notes

This framework is **tool-agnostic** by design, but different AI platforms may require minor tweaks:

- **Antigravity**: Automatically detects `.agent/` folder and workflows. Slash commands work out of the box.
- **Claude Code**: Reference agents directly: "Act as ResearchAgent from `2. Agents/ResearchAgent.md`"
- **Cursor**: Works natively with file context. Point to `AGENTS.md` in your first message.
- **Gemini**: Create `GEMINI.md` symlink to `AGENTS.md` (instructions in SETUP.md)
- **Custom setups**: You may need to adjust symlinks or add platform-specific config files

See `SETUP.md` for detailed platform setup instructions.

## About This Project

This is a personal framework I refined for my own business and decided to share as a template. It is not an actively maintained open-source project, so I am not accepting pull requests. Feel free to fork it and make it your own!

## Need Help Getting Started?

I built this system for my own business. If you're an SMB or solo operator looking to implement this framework but need guidance on:

- Adapting the architecture to your specific business
- Building custom skills for your workflows
- Setting this up for a team of users
- Training your team to use agent-driven operations
- Integrating with your existing tools and systems

**I'm available for consulting engagements to help you set this up.**

Reach out to me on [LinkedIn](https://www.linkedin.com/in/rick-lee/) to start the conversation.

I believe every small business should have access to sophisticated AI operations, and I'm here to help make that happen.

## License

MIT License - see LICENSE file for details.

## Learn More

- **Full Documentation**: See `AGENTS.md`
- **Setup Guide**: See `SETUP.md`
- **Example Skills**: Explore `3. Skills/`


