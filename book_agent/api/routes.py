"""Book Agent API routes.

The route layer keeps HTTP concerns separate from agent logic.
"""


def chat_endpoint(message: str):
    return {
        "message": message,
        "agent": "orchestrator"
    }


def books_endpoint():
    return []
