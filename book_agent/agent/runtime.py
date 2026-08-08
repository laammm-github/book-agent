from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AgentContext:
    """Shared state passed through the agent workflow."""

    query: str
    history: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class AgentRuntime:
    """Minimal runtime for future planner/executor based agents.

    This provides the foundation for adding planning, tools, memory and
    knowledge retrieval without coupling the orchestration layer.
    """

    def __init__(self, planner=None, executor=None):
        self.planner = planner
        self.executor = executor

    def run(self, query: str) -> Dict[str, Any]:
        context = AgentContext(query=query)

        if self.planner:
            plan = self.planner.create_plan(context)
        else:
            plan = {"steps": ["answer_query"]}

        if self.executor:
            result = self.executor.execute(plan, context)
        else:
            result = {"message": "Agent runtime initialized", "plan": plan}

        return result
