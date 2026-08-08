"""Tool discovery registry."""

from typing import Dict, Type

from .base import Tool


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: Dict[str, Type[Tool]] = {}

    def register(self, tool: Type[Tool]) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Type[Tool] | None:
        return self._tools.get(name)

    def list_tools(self) -> list[str]:
        return list(self._tools.keys())
