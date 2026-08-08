class MemoryStore:
    """Simple memory abstraction. Can later connect vector database."""

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def search(self, keyword):
        return [i for i in self.items if keyword in str(i)]
