"""Discover all tools available on the Hermes agent."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient
from ..helpers.tool_mapper import ToolMapper

class HermesListToolsTool(Tool):
    """Query Hermes for its tool registry and return mapped A0 tools."""
    async def execute(self, **kwargs) -> Response:
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 60)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            tools = await client.list_tools()
            mapped = ToolMapper.hermes_to_a0(tools)
            names = [t["name"] for t in mapped]
            msg = f"Discovered {len(names)} Hermes tools."
            if names:
                msg += "\n" + ", ".join(names)
            return Response(message=msg, break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes list_tools error: {str(e)}", break_loop=False)
