# SOP: Add MCP Server

## Goal
Add a new Model Context Protocol (MCP) server to the agent system, making it available to agents that need it.

## Context
MCP servers extend agent capabilities by connecting to external tools and services (GitHub, databases, APIs, etc.). The configuration lives in `.agent/mcp_config.json`.

## Process

### 1. Identify the MCP Server
- Determine which MCP server you need (e.g., `github`, `postgres`, `slack`)
- Find the server's npm package or installation method
- Note any required environment variables or API keys

### 2. Update Configuration
Edit `.agent/mcp_config.json` and add the server under `mcpServers`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### 3. Set Environment Variables
If the server requires API keys or tokens:
1. Add them to `.env` file
2. Ensure `.env` is in `.gitignore`
3. Create `.env.example` with placeholder values for documentation

### 4. Grant Agent Permissions
Edit the relevant agent file in `Operator Team OS/2. Agents/[AgentName].md` and add the tool to their `tools:` list:

```yaml
tools:
  - github
  - other-existing-tools
```

### 5. Test the Integration
- Restart your AI agent platform
- Verify the agent can access the new MCP server
- Test basic functionality

## Edge Cases
- **Missing API keys**: The agent will fail silently or throw authentication errors
- **npm package not found**: Verify the package name and version
- **Permission issues**: Remember to add the tool to BOTH `.agent/mcp_config.json` AND the agent's persona file

## Expected Output
- MCP server successfully added to configuration
- Agent can use the new tool
- Environment variables properly configured
