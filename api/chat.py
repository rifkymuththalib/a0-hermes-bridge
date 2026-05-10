from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient

class HermesChatApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        config = await self.get_plugin_config()
        prompt = input.get("prompt", "")
        model = input.get("model", config.get("default_model", "hermes-default"))
        if not prompt:
            return {"error": "prompt is required"}, 400
        client = HermesClient(
            base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
            api_key=config.get("api_key") or None,
            timeout=config.get("timeout_seconds", 60)
        )
        try:
            result = await client.chat(messages=[{"role": "user", "content": prompt}], model=model)
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            return {"result": content, "model": model}
        except Exception as e:
            return {"error": str(e)}, 500
