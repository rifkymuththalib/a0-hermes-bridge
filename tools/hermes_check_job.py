"""Check the status of a Hermes background job by job_id."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient

class HermesCheckJobTool(Tool):
    """Poll a Hermes background job for status."""
    async def execute(self, **kwargs) -> Response:
        job_id = kwargs.get("job_id", "")
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 60)

        if not job_id:
            return Response(message="Error: job_id is required", break_loop=False)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            result = await client.get_job(job_id)
            status = result.get("status", "unknown")
            progress = result.get("progress", "")
            msg = f"Job {job_id} status: {status}"
            if progress:
                msg += f" | Progress: {progress}"
            return Response(message=msg, break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes check_job error: {str(e)}", break_loop=False)
