"""Route a tool call through the Hermes MCP gateway (Phase 2)."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient

class HermesMcpProxyTool(Tool):
    """Proxy a tool call through Hermes MCP server."""
    async def execute(self, **kwargs) -> Response:
        server_id = kwargs.get("server_id", "")
        tool_name = kwargs.get("tool_name", "")
        arguments = kwargs.get("arguments", {})
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 60)

        if not server_id or not tool_name:
            return Response(message="Error: server_id and tool_name are required", break_loop=False)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            result = await client.mcp_call_tool(server_id, tool_name, arguments)
            return Response(message=str(result.get("result", result)), break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes MCP proxy error: {str(e)}", break_loop=False)
