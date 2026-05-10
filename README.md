# 🤝 Hermes Agent Bridge for Agent Zero

Bridge Agent Zero with a Hermes Agent instance to delegate tasks, invoke skills, and share tools.

## Features

- 🔌 **HTTP API Client** — Connect to Hermes via OpenAI-compatible HTTP API
- 🧰 **Tool Discovery** — Auto-sync Hermes tools into A0 with `hermes_` prefix
- 🎭 **Skill Invocation** — Run Hermes skills by name
- 🚀 **Job Delegation** — Submit background jobs and poll status
- 🧠 **Memory Search** — Query Hermes persistent memory
- 🤖 **Subordinate Agent** — Spawn Hermes as a subordinate with task context
- ⚙️ **Configuration UI** — Post-install settings panel
- 📊 **Real-time Dashboard** — Monitor status, latency, tool count

## Installation

1. Clone to `/a0/usr/plugins/hermes_bridge/`
2. Open **Plugin Settings** and enter your Hermes endpoint
3. Click **Test Connection**
4. (Optional) Enable **Auto-discover tools**

## Tools (8)

| Tool | Purpose |
|------|---------|
| `hermes_chat` | Chat with Hermes |
| `hermes_list_tools` | Discover Hermes tools |
| `hermes_run_skill` | Invoke a Hermes skill |
| `hermes_run_job` | Submit a background job |
| `hermes_check_job` | Poll job status |
| `hermes_subagent` | Spawn Hermes subordinate |
| `hermes_mcp_proxy` | Proxy via MCP gateway |
| `hermes_memory_search` | Search Hermes memory |

## API Endpoints (15)

All under `/api/plugins/hermes_bridge/`

`status`, `chat`, `jobs`, `submit_job`, `check_job`, `stop_job`, `run_skill`, `sync_tools`, `sync_skills`, `sync_memory`, `mcp_servers`, `mcp_test`, `config`, `logs`, `deploy`, `stop`

## License

MIT © Rifky Muththalib
