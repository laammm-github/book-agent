from book_agent.knowledge.parser import BookParser
from book_agent.knowledge.vector_store import VectorStore
from book_agent.rag.engine import RAGEngine

parser = BookParser()
doc = parser.parse_text("Demo Book", "AI changes how humans learn")

store = VectorStore()
for chunk in parser.split_chunks(doc):
    store.add(chunk)

rag = RAGEngine(store)
print(rag.answer("What is this book about?"))
