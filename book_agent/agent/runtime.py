"""Core runtime that connects lifecycle, executor and registries."""

from .context import AgentContext
from .executor import AgentExecutor
from .lifecycle import LifecycleManager


class AgentRuntime:
    """Coordinate agent execution with lifecycle and capability registries."""

    def __init__(self, skill_registry=None, tool_registry=None):
        self.agents = {}
        self.context = AgentContext()
        self.lifecycle = LifecycleManager()
        self.executor = AgentExecutor(
            skill_registry=skill_registry,
            tool_registry=tool_registry,
        )

    def register(self, agent):
        self.agents[agent.name] = agent

    def start(self):
        self.lifecycle.start()

    def stop(self):
        self.lifecycle.stop()

    def run(self, task: str, agent_name: str | None = None, context=None):
        if not self.lifecycle.is_running():
            self.start()

        execution_context = context or self.context

        if agent_name:
            if agent_name not in self.agents:
                raise ValueError(f"Unknown agent: {agent_name}")
            return self.agents[agent_name].run(task, execution_context)

        return self.executor.execute(task, execution_context)
