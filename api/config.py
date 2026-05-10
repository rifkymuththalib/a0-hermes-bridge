from helpers.api import ApiHandler
from flask import Request

class HermesConfigApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["GET", "POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        if request.method in ("GET", "HEAD"):
            config = await self.get_plugin_config()
            return {"config": config}
        await self.set_plugin_config(input)
        return {"success": True, "config": input}
