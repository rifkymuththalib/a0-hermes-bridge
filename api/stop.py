from helpers.api import ApiHandler
from flask import Request

class HermesStopApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["POST", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        return {"status": "stopped", "message": "Hermes bridge plugin disconnect signal sent."}
