# Setup Guide

This guide will help you get the Operator OS running in your environment.

> **Tip**: You can ask your AI to help you with setup. Just say "Read SETUP.md and help me get started." The AI can walk you through these steps and handle the technical details.

## Prerequisites

- **Python 3.9+** (for skills that use Python scripts)
- **Node.js 18+** (for MCP servers)
- **Git** (for version control)
- **An AI platform** that supports file context:
  - Anthropic Claude (via API or Code)
  - Google Gemini
  - Cursor
  - Antigravity
  - Similar agent frameworks

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/operator-os.git
cd operator-os
```

**Windows Users**: Git may not create symlinks correctly by default. Run this before cloning:
```bash
git config --global core.symlinks true
```

Or manually create the symlinks after cloning:
```bash
# From the repo root
mklink CLAUDE.md AGENTS.md
mklink GEMINI.md AGENTS.md
cd .agent
mklink /D workflows "..\4. Workflows"
```

### 2. Set Up Environment Variables (Optional)

**Most users can skip this step.** If you're using Claude Code, Antigravity, Cursor, or similar platforms, the AI handles its own API calls—you don't need to configure anything.

You only need a `.env` file if:
- You're using MCP servers that require authentication (GitHub, Slack, etc.)
- You're building custom skills that call external APIs

If you do need it:

```bash
cp .env.example .env
```

Example `.env` contents:

```env
# Only add what you actually need:
GITHUB_TOKEN=your_token_here      # For GitHub MCP server
SLACK_TOKEN=your_token_here       # For Slack MCP server
OPENROUTER_API_KEY=your_key_here  # For custom skills that call LLMs
```

**Important**: Never commit `.env` to version control. It's already in `.gitignore`.

### 3. Install Python Dependencies (Optional)

If you plan to run the skills that use Python scripts:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

> **Note**: Some skills include their own `requirements.txt`. Install as needed.

### 4. Configure MCP Servers (Optional)

MCP (Model Context Protocol) lets AI platforms connect to external tools like GitHub, Slack, or databases.

**Each platform handles MCP differently.** Check your platform's documentation:
- Antigravity, Claude Code, and similar tools have their own MCP configuration methods
- Some platforms auto-detect servers, others require manual setup
- The `.agent/mcp_config.json` file in this repo is an example that works with Antigravity. Your platform may use a different location or format

### 5. Set Up Workflows (Optional)

If using Antigravity or platforms that support slash commands:

The workflows are already symlinked:
```
.agent/workflows/ → 4. Workflows/
```

If you need to recreate the symlink:
```bash
cd .agent/workflows
ln -s ../../4. Workflows/* .
```

## Platform-Specific Setup

### For Anthropic Claude (API)

The repository includes a `CLAUDE.md` file that symlinks to `AGENTS.md`. Claude-based platforms will automatically detect this.

```python
import anthropic

client = anthropic.Anthropic(api_key="your_key")

# Point Claude to the CLAUDE.md file (or AGENTS.md)
with open("CLAUDE.md", "r") as f:
    system_prompt = f.read()

# Use in your agent loop
```

### For Google Gemini

The repository includes a `GEMINI.md` file that symlinks to `AGENTS.md`. Gemini-based platforms will automatically detect this.

If the symlink doesn't work on your system:
```bash
# Create the symlink manually
ln -s AGENTS.md GEMINI.md
```

### For Cursor

1. Open Cursor in the `operator-os` directory
2. The AI will automatically see all files
3. In your first message, reference: "Read `AGENTS.md` to understand the system architecture"
4. Reference specific agents: "Act as the Research Agent defined in `2. Agents/ResearchAgent.md`"

### For Antigravity

1. Antigravity automatically recognizes `.agent/` folder
2. Workflows are already symlinked to `.agent/workflows/`
3. Use workflows with `/` commands: `/consult-board`, `/weekly-review`
4. MCP servers auto-load from `.agent/mcp_config.json`


## First Steps

### 1. Read AGENTS.md

This is the core document. It explains:
- The 5-layer architecture
- How layers interact
- Operating principles
- File organization rules

```bash
# Read in your terminal
cat AGENTS.md

# Or open in your editor
```

### 2. Explore the Examples

**SOPs**: Check out `1. SOPs/` to see how to document processes

**Agents**: Review `2. Agents/Board-Strategy.md` to see a persona definition

**Skills**: Look at `3. Skills/pdf-conversion/` to see how skills are structured

**Workflows**: Try `/consult-board` to ask strategic questions

## Customize for Your Needs

### Add Your Own SOPs

Create a new file in `1. SOPs/`:

```bash
touch "1. SOPs/my-custom-process.md"
```

Follow the template structure:
- Goal
- Context
- Inputs
- Outputs
- Process steps
- Edge cases
- Expected output

### Create Custom Agents

Create a new agent in `2. Agents/`:

```bash
touch "2. Agents/MyCustomAgent.md"
```

Define:
- Purpose
- Persona & expertise
- Voice & style
- Model preference
- Tools they can use
- Decision-making approach
- Output format
- Guardrails

### Build New Skills

This repo includes example skills from [Anthropic's skills repository](https://github.com/anthropics/skills), including document creation (docx, xlsx, pptx) and PDF conversion.

**Find more skills:**
- [Anthropic's official skills](https://github.com/anthropics/skills) - Official skills from Anthropic
- [Superpowers](https://github.com/obra/superpowers) - Community skills collection
- [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills) - Curated list of skills

To build your own, use the `skill-creator` meta-skill:

```
Agent: "Create a new skill for [task description]"
```

Or manually:
```bash
mkdir "3. Skills/my-new-skill"
touch "3. Skills/my-new-skill/SKILL.md"
mkdir "3. Skills/my-new-skill/scripts"
```

### Add Workflows

Create a workflow in `4. Workflows/`:

```bash
touch "4. Workflows/my-workflow.md"
```

Format:
```yaml
---
description: Short description of what this does
---

## Steps

1. First thing to do
2. Second thing to do
// turbo  ← Optional: auto-run this step
3. Third thing to do
```

## Troubleshooting

### Agent Can't Find Files
- **Check**: Are you in the right directory?
- **Fix**: Use absolute paths or ensure the agent's working directory is correct

### MCP Server Not Loading
- **Check**: Is the server in `.agent/mcp_config.json`?
- **Check**: Are environment variables set in `.env`?
- **Fix**: Restart your AI platform after config changes

### Python Script Errors
- **Check**: Did you activate the virtual environment?
- **Check**: Are dependencies installed?
- **Fix**: `pip install -r requirements.txt`

### Workflows Not Showing Up
- **Check**: Is `.agent/workflows/` symlinked correctly?
- **Fix**: `cd .agent/workflows && ln -s ../../4. Workflows/* .`

## Advanced Configuration

### Dynamic Drive Paths

Use `drive_path.py` to avoid hardcoding folder names:

```python
from drive_path import get_drive_path

drive_name = get_drive_path()  # Returns "Drive - ProjectX"
file_path = f"{drive_name}/Data/myfile.csv"
```

### Self-Annealing

When scripts break:
1. Agent reads error
2. Fixes the script
3. Tests the fix
4. Updates SKILL.md with lessons learned

Enable this by telling your agent: "Self-anneal when errors occur (see AGENTS.md)"

## Next Steps

1. **Customize**: Replace "ProjectX" with your actual project name
2. **Build**: Add your own SOPs, agents, and skills
3. **Share**: If you build something cool, contribute back!
4. **Join the community**: [Add Discord/forum link]

## Getting Help

- **Documentation**: Read `AGENTS.md` thoroughly
- **Examples**: Study the included skills and SOPs
- **Issues**: Open a GitHub issue if you find bugs
- **Community**: Share your use case and get help from others

---

**Ready to build?** Just start a conversation with your AI and tell it what you need!
