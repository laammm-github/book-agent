from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentContext:
    """Runtime context shared during an agent execution."""

    user_id: str | None = None
    book: str | None = None
    history: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
