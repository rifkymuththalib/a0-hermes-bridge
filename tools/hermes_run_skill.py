"""Run a specific skill on the Hermes agent by name with a prompt."""
from helpers.tool import Tool, Response
from ..helpers.client import HermesClient

class HermesRunSkillTool(Tool):
    """Invoke a Hermes skill by name."""
    async def execute(self, **kwargs) -> Response:
        skill_name = kwargs.get("skill_name", "")
        prompt = kwargs.get("prompt", "")
        base_url = kwargs.get("base_url", "http://127.0.0.1:8642")
        api_key = kwargs.get("api_key", None)
        timeout = kwargs.get("timeout", 60)

        if not skill_name:
            return Response(message="Error: skill_name is required", break_loop=False)

        client = HermesClient(base_url=base_url, api_key=api_key, timeout=timeout)
        try:
            result = await client.run_skill(skill_name, prompt)
            content = result.get("result", result.get("content", str(result)))
            return Response(message=f"Skill '{skill_name}' result:\n{content}", break_loop=False)
        except Exception as e:
            return Response(message=f"Hermes run_skill error: {str(e)}", break_loop=False)
