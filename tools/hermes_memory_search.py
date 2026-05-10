"""Search the Hermes agent memory store for relevant entries."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient

class HermesMemorySearchTool(Tool):
    """Query Hermes memory store for past facts or solutions."""
    async def execute(self, **kwargs) -> Response:
        query = kwargs.get("query", "")
        limit = kwargs.get("limit", 10)
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 60)

        if not query:
            return Response(message="Error: query is required", break_loop=False)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            results = await client.search_memory(query=query, limit=limit)
            if not results:
                return Response(message="No memory entries found.", break_loop=False)
            lines = [f"- {r.get('content', r)}" for r in results[:limit]]
            return Response(message="Memory results:\n" + "\n".join(lines), break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes memory search error: {str(e)}", break_loop=False)
