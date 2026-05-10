from helpers.api import ApiHandler
from flask import Request

class HermesLogsApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["GET", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        return {"logs": "Hermes logs endpoint not yet implemented in HTTP bridge mode"}
