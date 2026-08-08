from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class AgentContext:
    """Runtime context shared during an agent execution.

    Provides extension points for future memory systems.
    """

    session_id: str | None = None
    user_id: str | None = None
    task: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    history: list[str] = field(default_factory=list)
    memory_hooks: list[Callable[["AgentContext"], Any]] = field(default_factory=list)
    book: str | None = None

    def add_history(self, item: str) -> None:
        self.history.append(item)

    def add_memory_hook(self, hook: Callable[["AgentContext"], Any]) -> None:
        self.memory_hooks.append(hook)
