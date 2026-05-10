from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient

class HermesStatusApi(ApiHandler):
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
            health = await client.health()
            tools = await client.list_tools()
            skills = await client.list_skills()
            return {
                "connected": health.get("healthy", False),
                "latency_ms": 0,
                "tool_count": len(tools),
                "skills_count": len(skills),
                "base_url": config.get("hermes_base_url", ""),
                "mode": config.get("connection_mode", "http_api")
            }
        except Exception as e:
            return {"connected": False, "error": str(e), "base_url": config.get("hermes_base_url", "")}
