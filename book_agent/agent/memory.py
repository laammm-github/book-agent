from .base import BaseAgent


class MemoryAgent(BaseAgent):
    """Long term reading memory manager."""

    name = "memory"

    def __init__(self):
        self.storage = []

    def run(self, task: str):
        self.storage.append(task)
        return {
            "agent": self.name,
            "memory_size": len(self.storage)
        }
