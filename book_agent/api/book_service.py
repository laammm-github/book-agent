"""Book ingestion service for the MVP workflow."""

from dataclasses import dataclass


@dataclass
class BookInput:
    title: str
    content: str


class BookService:
    def __init__(self, parser=None, vector_store=None):
        self.parser = parser
        self.vector_store = vector_store

    def ingest(self, book: BookInput):
        """Prepare a book for indexing."""
        if self.parser is None:
            return {"title": book.title, "chunks": []}

        document = self.parser.parse_text(book.title, book.content)
        chunks = self.parser.split_chunks(document)

        if self.vector_store:
            self.vector_store.add(chunks)

        return {"title": book.title, "chunks": chunks}
