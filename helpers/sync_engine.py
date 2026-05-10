"""Sync engine for tools, skills, and memory between A0 and Hermes."""
from .client import HermesClient
from .tool_mapper import ToolMapper

class SyncEngine:
    def __init__(self, client: HermesClient):
        self.client = client

    async def sync_tools(self) -> dict:
        try:
            hermes_tools = await self.client.list_tools()
            mapped = ToolMapper.hermes_to_a0(hermes_tools)
            return {"synced": len(mapped), "tools": mapped}
        except Exception as e:
            return {"synced": 0, "error": str(e)}

    async def sync_skills(self) -> dict:
        try:
            skills = await self.client.list_skills()
            return {"synced": len(skills), "skills": skills}
        except Exception as e:
            return {"synced": 0, "error": str(e)}

    async def sync_memory(self, query: str = "", limit: int = 10) -> dict:
        try:
            results = await self.client.search_memory(query=query, limit=limit)
            return {"synced": len(results), "results": results}
        except Exception as e:
            return {"synced": 0, "error": str(e)}
