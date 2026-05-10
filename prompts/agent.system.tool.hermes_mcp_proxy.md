## hermes_mcp_proxy

Route a tool call through the Hermes MCP (Model Context Protocol) gateway.

### Parameters
- **server_id** (string, required): MCP server identifier.
- **tool_name** (string, required): Name of the tool to call on the MCP server.
- **arguments** (object, default: {}): Tool arguments.
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token.
- **timeout** (number, default: 60): Request timeout.

### Example
```json
{"tool_name": "hermes_mcp_proxy", "tool_args": {"server_id": "local-fs", "tool_name": "read_file", "arguments": {"path": "/tmp/test.txt"}}}
```

### Returns
MCP tool execution result or error message.
