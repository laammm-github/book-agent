class KnowledgeGraph:
    """Knowledge relationship storage."""

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, name, data=None):
        self.nodes[name] = data or {}

    def connect(self, source, target, relation):
        self.edges.append({
            "source": source,
            "target": target,
            "relation": relation
        })
