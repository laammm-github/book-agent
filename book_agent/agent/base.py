from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Base class for all book agents."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, task: str):
        """Execute an agent task."""
        raise NotImplementedError
