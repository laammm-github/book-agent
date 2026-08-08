from .context import AgentContext


class AgentRuntime:
    """Coordinate task execution between user requests and agents."""

    def __init__(self):
        self.agents = {}

    def register(self, agent):
        self.agents[agent.name] = agent

    def run(self, task: str, agent_name: str, context: AgentContext | None = None):
        context = context or AgentContext()

        if agent_name not in self.agents:
            raise ValueError(f"Unknown agent: {agent_name}")

        return self.agents[agent_name].run(task, context)
