## hermes_memory_search

Search the Hermes agent persistent memory store for relevant entries.

### Parameters
- **query** (string, required): Search query string.
- **limit** (number, default: 10): Maximum results to return.
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token.
- **timeout** (number, default: 60): Request timeout.

### Example
```json
{"tool_name": "hermes_memory_search", "tool_args": {"query": "docker compose setup"}}
```

### Returns
List of matching memory entries or "No entries found" message.
