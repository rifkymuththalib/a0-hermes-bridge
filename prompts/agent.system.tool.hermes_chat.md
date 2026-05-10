## hermes_chat

Send a chat message to a Hermes Agent instance and return the response.

### Parameters
- **prompt** (string, required): The message to send to Hermes.
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token for authentication.
- **timeout** (number, default: 60): Request timeout in seconds.
- **model** (string, default: "hermes-default"): Model to use.

### Example
```json
{"tool_name": "hermes_chat", "tool_args": {"prompt": "Explain quantum computing"}}
```

### Returns
Hermes response text or error message.
