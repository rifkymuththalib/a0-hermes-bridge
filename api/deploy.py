from helpers.api import ApiHandler
from flask import Request

class HermesDeployApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        return {"status": "not_deployed", "message": "Hermes bridge plugin is configured-only. Ensure Hermes Agent is running at the configured base_url."}
