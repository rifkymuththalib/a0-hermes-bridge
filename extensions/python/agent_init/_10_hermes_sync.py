from helpers.extension import Extension

class HermesBridgeInitExtension(Extension):
    async def execute(self, **kwargs) -> None:
        agent = self.agent
        try:
            config = agent.context.data.get("hermes_bridge_config", {})
            if config.get("auto_discover_tools", True):
                from ....helpers.client import HermesClient
                from ....helpers.tool_mapper import ToolMapper
                client = HermesClient(
                    base_url=config.get("hermes_base_url", "http://127.0.0.1:8642"),
                    api_key=config.get("api_key") or None,
                    timeout=config.get("timeout_seconds", 60)
                )
                tools = await client.list_tools()
                mapped = ToolMapper.hermes_to_a0(tools)
                print(f"[Hermes Bridge] Auto-synced {len(mapped)} tools")
        except Exception:
            pass
