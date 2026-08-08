"""Agent execution pipeline primitives."""


class AgentExecutor:
    def __init__(self, skill_registry=None, tool_registry=None):
        self.skill_registry = skill_registry
        self.tool_registry = tool_registry

    def execute(self, task, context=None):
        """Execute a task through registered capabilities.

        The concrete planning policy will be provided by the LLM adapter layer.
        """
        return {
            "task": task,
            "context": context,
            "status": "accepted",
        }
