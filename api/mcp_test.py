from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient

class HermesMcpTestApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        config = await self.get_plugin_config()
        server_id = input.get("server_id", "")
        if not server_id:
            return {"error": "server_id is required"}, 400
        client = HermesClient(
            base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
            api_key=config.get("api_key") or None,
            timeout=config.get("timeout_seconds", 60)
        )
        try:
            result = await client.mcp_test(server_id)
            return {"server_id": server_id, "test_result": result}
        except Exception as e:
            return {"error": str(e)}, 500
