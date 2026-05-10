from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient

class HermesSyncMemoryApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        config = await self.get_plugin_config()
        query = input.get("query", "")
        limit = input.get("limit", 10)
        client = HermesClient(
            base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
            api_key=config.get("api_key") or None,
            timeout=config.get("timeout_seconds", 60)
        )
        try:
            results = await client.search_memory(query=query, limit=limit)
            return {"synced": len(results), "results": results}
        except Exception as e:
            return {"error": str(e)}, 500
