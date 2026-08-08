from dataclasses import dataclass, field


@dataclass
class Chapter:
    title: str
    content: str
    index: int = 0


@dataclass
class Book:
    title: str
    author: str | None = None
    chapters: list[Chapter] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
