"""Build context for RAG generation."""


class ContextBuilder:
    def build(self, question, documents):
        return {
            "question": question,
            "context": "\n".join(documents),
        }
