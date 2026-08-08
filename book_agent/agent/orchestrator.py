from .base import BaseAgent


class OrchestratorAgent(BaseAgent):
    """Routes reading tasks to specialized agents."""

    def __init__(self):
        super().__init__("orchestrator")

    def run(self, task: str):
        return {
            "agent": self.name,
            "task": task,
            "status": "planned"
        }
