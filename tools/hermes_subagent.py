"""Spawn Hermes as a subordinate agent with a task and optional context."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient

class HermesSubagentTool(Tool):
    """Delegate a task to Hermes as a subordinate agent."""
    async def execute(self, **kwargs) -> Response:
        task = kwargs.get("task", "")
        context = kwargs.get("context", "")
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 120)
        model = kwargs.get("model", "hermes-default")

        if not task:
            return Response(message="Error: task is required", break_loop=False)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            system_msg = "You are a specialist subordinate agent. Complete the given task precisely."
            if context:
                system_msg += "\nContext: " + context
            messages = [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": task}
            ]
            result = await client.chat(messages=messages, model=model)
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            return Response(message=content, break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes subagent error: {str(e)}", break_loop=False)
