from .base import BaseAgent


class ReaderAgent(BaseAgent):
    """Book comprehension and Q&A agent."""

    def __init__(self):
        super().__init__("reader")

    def run(self, task: str):
        return {
            "agent": self.name,
            "task": task,
            "response": "Reader agent ready"
        }
