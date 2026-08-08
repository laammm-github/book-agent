from .base import BaseAgent


class ReaderAgent(BaseAgent):
    """Book comprehension and Q&A agent."""

    def __init__(self):
        super().__init__("reader")

    def run(self, task: str, context=None):
        return {
            "agent": self.name,
            "task": task,
            "book": getattr(context, "book", None),
            "response": "Reader agent ready"
        }
