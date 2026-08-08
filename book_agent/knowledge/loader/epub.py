from .base import BookLoader
from ..models.book import Book


class EPUBLoader(BookLoader):
    def load(self, path: str) -> Book:
        return Book(title=path, metadata={"format": "epub", "source": path})
