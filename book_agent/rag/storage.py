"""Vector storage abstractions."""


class VectorStore:
    """Simple vector storage interface."""

    def __init__(self):
        self.items = []

    def add(self, vector: list[float], payload: dict):
        self.items.append((vector, payload))

    def search(self, vector: list[float], top_k: int = 3):
        return [item[1] for item in self.items[:top_k]]
