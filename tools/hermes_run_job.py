"""Start a background job on the Hermes agent. Returns a job_id."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient

class HermesRunJobTool(Tool):
    """Submit a background job to Hermes."""
    async def execute(self, **kwargs) -> Response:
        prompt = kwargs.get("prompt", "")
        schedule = kwargs.get("schedule", None)
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 60)

        if not prompt:
            return Response(message="Error: prompt is required", break_loop=False)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            result = await client.run_job(prompt, schedule=schedule)
            job_id = result.get("job_id", result.get("id", "unknown"))
            return Response(message=f"Job started. ID: {job_id}", break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes run_job error: {str(e)}", break_loop=False)
