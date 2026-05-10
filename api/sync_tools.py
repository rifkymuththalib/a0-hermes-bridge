from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient
from ..helpers.tool_mapper import ToolMapper

class HermesSyncToolsApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        config = await self.get_plugin_config()
        client = HermesClient(
            base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
            api_key=config.get("api_key") or None,
            timeout=config.get("timeout_seconds", 60)
        )
        try:
            tools = await client.list_tools()
            mapped = ToolMapper.hermes_to_a0(tools)
            return {"synced": len(mapped), "tools": mapped}
        except Exception as e:
            return {"error": str(e)}, 500
