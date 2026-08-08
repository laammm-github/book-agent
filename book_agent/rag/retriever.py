"""Retrieval layer for RAG pipeline."""


class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query: str):
        return self.vector_store.search(query)
