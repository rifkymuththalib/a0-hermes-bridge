"""Maps Hermes OpenAI-format tool schemas to Agent Zero tool schemas."""
from typing import Any

class ToolMapper:
    @staticmethod
    def hermes_to_a0(hermes_tools: list[dict]) -> list[dict]:
        mapped = []
        for tool in hermes_tools:
            if not isinstance(tool, dict):
                continue
            func = tool.get("function") or tool.get("tool")
            if not func:
                continue
            name = func.get("name", "")
            if not name:
                continue
            mapped.append({
                "name": f"hermes_{name}",
                "description": f"[Hermes] {func.get('description', '')}",
                "parameters": func.get("parameters", {"type": "object", "properties": {}}),
            })
        return mapped

    @staticmethod
    def validate_schema(tool: dict) -> bool:
        params = tool.get("parameters", {})
        props = params.get("properties", {})
        for key, val in props.items():
            ptype = val.get("type", "string")
            if ptype in ("file", "binary", "blob"):
                return False
        return True
