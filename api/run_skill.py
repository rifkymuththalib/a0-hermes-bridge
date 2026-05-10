from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient

class HermesRunSkillApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        config = await self.get_plugin_config()
        skill_name = input.get("skill_name", "")
        prompt = input.get("prompt", "")
        if not skill_name:
            return {"error": "skill_name is required"}, 400
        client = HermesClient(
            base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
            api_key=config.get("api_key") or None,
            timeout=config.get("timeout_seconds", 60)
        )
        try:
            result = await client.run_skill(skill_name, prompt)
            return {"skill": skill_name, "result": result.get("result", result.get("content", str(result)))}
        except Exception as e:
            return {"error": str(e)}, 500
