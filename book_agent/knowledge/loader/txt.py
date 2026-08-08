from .base import BookLoader
from ..models.book import Book


class TXTLoader(BookLoader):
    def load(self, path: str) -> Book:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return Book(title=path, metadata={"format": "txt", "content": content})
