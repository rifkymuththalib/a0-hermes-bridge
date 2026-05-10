## hermes_run_skill

Invoke a named skill on the Hermes Agent with a prompt.

### Parameters
- **skill_name** (string, required): Name of the Hermes skill to run.
- **prompt** (string, default: ""): Input prompt for the skill.
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token.
- **timeout** (number, default: 60): Request timeout.

### Example
```json
{"tool_name": "hermes_run_skill", "tool_args": {"skill_name": "web_search", "prompt": "latest AI news"}}
```

### Returns
Skill execution result or error message.
