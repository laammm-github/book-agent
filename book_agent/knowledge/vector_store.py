"""Vector retrieval abstraction."""


class VectorStore:
    def __init__(self):
        self.items = []

    def add(self, text, metadata=None):
        self.items.append({"text": text, "metadata": metadata or {}})

    def search(self, query, top_k=3):
        return self.items[:top_k]
