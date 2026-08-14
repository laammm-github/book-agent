"""Book question answering retrieval flow."""


class BookQARetriever:
    def __init__(self, embedding, store):
        self.embedding = embedding
        self.store = store

    def answer_context(self, question: str, top_k: int = 3):
        vector = self.embedding.embed(question)
        return self.store.search(vector, top_k=top_k)
