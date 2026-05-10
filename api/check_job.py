from helpers.api import ApiHandler
from flask import Request
from ..helpers.client import HermesClient

class HermesCheckJobApi(ApiHandler):
    @classmethod
    def get_methods(cls): return ["GET", "OPTIONS", "HEAD"]

    async def process(self, input: dict, request: Request):
        config = await self.get_plugin_config()
        job_id = input.get("job_id", "")
        if not job_id:
            return {"error": "job_id is required"}, 400
        client = HermesClient(
            base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
            api_key=config.get("api_key") or None,
            timeout=config.get("timeout_seconds", 60)
        )
        try:
            result = await client.get_job(job_id)
            return {"job_id": job_id, "status": result.get("status", "unknown"),
                    "progress": result.get("progress", ""), "result": result.get("result", "")}
        except Exception as e:
            return {"error": str(e)}, 500
