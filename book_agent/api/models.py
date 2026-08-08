from dataclasses import dataclass


@dataclass
class ChatRequest:
    message: str


@dataclass
class BookCreateRequest:
    title: str
    content: str
