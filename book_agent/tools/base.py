"""Tool abstraction used by agents."""

from abc import ABC, abstractmethod


class Tool(ABC):
    name: str = "tool"

    @abstractmethod
    def execute(self, **kwargs):
        raise NotImplementedError
