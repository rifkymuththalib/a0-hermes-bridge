"""Send a chat message to Hermes and return the response."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient

class HermesChatTool(Tool):
    """Chat with Hermes Agent via its OpenAI-compatible API."""
    async def execute(self, **kwargs) -> Response:
        prompt = kwargs.get("prompt", "")
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 60)
        model = kwargs.get("model", "hermes-default")

        if not prompt:
            return Response(message="Error: prompt is required", break_loop=False)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            result = await client.chat(messages=[{"role": "user", "content": prompt}], model=model)
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            return Response(message=content, break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes chat error: {str(e)}", break_loop=False)
