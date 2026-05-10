## hermes_subagent

Spawn Hermes as a subordinate agent to handle a specific task with optional context.

### Parameters
- **task** (string, required): The task to delegate to Hermes.
- **context** (string, optional): Additional context or background info.
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token.
- **timeout** (number, default: 120): Request timeout (longer for subagent tasks).
- **model** (string, default: "hermes-default"): Model to use.

### Example
```json
{"tool_name": "hermes_subagent", "tool_args": {"task": "Find the best Python library for PDF parsing", "context": "Need OCR support and table extraction"}}
```

### Returns
Subordinate agent response or error message.
