"""Book Agent API server foundation."""

from typing import Dict


def health() -> Dict[str, str]:
    return {"status": "ok", "service": "book-agent"}


def chat(message: str) -> Dict[str, str]:
    return {
        "question": message,
        "answer": "Book Agent is ready to reason about your reading material."
    }
