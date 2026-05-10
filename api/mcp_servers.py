from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient

class HermesMcpServersApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["GET", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        config = await self.get_plugin_config()
        client = HermesClient(
            base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
            api_key=config.get("api_key") or None,
            timeout=config.get("timeout_seconds", 60)
        )
        try:
            servers = await client.mcp_servers()
            return {"servers": servers}
        except Exception as e:
            return {"error": str(e)}, 500
