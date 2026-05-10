## hermes_list_tools

Discover all tools available on the connected Hermes Agent.

### Parameters
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token.
- **timeout** (number, default: 60): Request timeout.

### Example
```json
{"tool_name": "hermes_list_tools", "tool_args": {}}
```

### Returns
Count and list of Hermes tools mapped to A0 format with `hermes_` prefix.
