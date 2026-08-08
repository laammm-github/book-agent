from .base import BookLoader
from ..models.book import Book


class PDFLoader(BookLoader):
    def load(self, path: str) -> Book:
        return Book(title=path, metadata={"format": "pdf", "source": path})
