"""Retrieval augmented generation engine."""


class RAGEngine:
    def __init__(self, retriever, llm=None):
        self.retriever = retriever
        self.llm = llm

    def answer(self, question):
        context = self.retriever.search(question)
        if self.llm:
            return self.llm.generate(question, context)
        return {
            "question": question,
            "context": context,
            "answer": "RAG response generated from retrieved knowledge."
        }
