"""Hermes Agent HTTP API client."""
import httpx
from typing import Any, Optional

class HermesClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8642", api_key: Optional[str] = None, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.headers = {}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

    async def chat(self, messages: list, model: str = "hermes-default", tools: Optional[list] = None, stream: bool = False) -> dict:
        payload = {"model": model, "messages": messages, "stream": stream}
        if tools:
            payload["tools"] = tools
        return await self._post("/v1/chat/completions", payload)

    async def responses(self, input_text: str, previous_response_id: Optional[str] = None) -> dict:
        payload = {"input": input_text}
        if previous_response_id:
            payload["previous_response_id"] = previous_response_id
        return await self._post("/v1/responses", payload)

    async def list_tools(self) -> list[dict]:
        r = await self._get("/v1/capabilities")
        return r.get("tools", []) if isinstance(r, dict) else r

    async def run_job(self, prompt: str, schedule: Optional[str] = None) -> dict:
        payload = {"prompt": prompt}
        if schedule:
            payload["schedule"] = schedule
        return await self._post("/api/jobs", payload)

    async def get_job(self, job_id: str) -> dict:
        return await self._get(f"/api/jobs/{job_id}")

    async def stop_job(self, job_id: str) -> dict:
        return await self._post(f"/api/jobs/{job_id}/stop", {})

    async def health(self) -> dict:
        try:
            r = await self._get("/health")
            return {"healthy": True, "status": r}
        except Exception as e:
            return {"healthy": False, "error": str(e)}

    async def run_skill(self, skill_name: str, prompt: str) -> dict:
        return await self._post(f"/api/skills/{skill_name}", {"prompt": prompt})

    async def list_skills(self) -> list[dict]:
        r = await self._get("/api/skills")
        return r if isinstance(r, list) else r.get("skills", [])

    async def search_memory(self, query: str, limit: int = 10) -> list[dict]:
        r = await self._get("/api/memory", params={"query": query, "limit": limit})
        return r if isinstance(r, list) else r.get("results", [])

    async def mcp_servers(self) -> list[dict]:
        r = await self._get("/api/mcp/servers")
        return r if isinstance(r, list) else r.get("servers", [])

    async def mcp_test(self, server_id: str) -> dict:
        return await self._post("/api/mcp/test", {"server_id": server_id})

    async def mcp_call_tool(self, server_id: str, tool_name: str, arguments: dict) -> dict:
        return await self._post("/api/mcp/tools", {
            "server_id": server_id, "tool_name": tool_name, "arguments": arguments
        })

    async def _get(self, path: str, params: Optional[dict] = None) -> Any:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            url = f"{self.base_url}{path}"
            r = await client.get(url, headers=self.headers, params=params)
            r.raise_for_status()
            return r.json()

    async def _post(self, path: str, payload: dict) -> Any:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            url = f"{self.base_url}{path}"
            r = await client.post(url, headers={**self.headers, "Content-Type": "application/json"}, json=payload)
            r.raise_for_status()
            return r.json()
