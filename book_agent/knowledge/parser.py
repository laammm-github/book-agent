"""Book document parsing utilities."""

from dataclasses import dataclass


@dataclass
class Document:
    title: str
    content: str


class BookParser:
    """Convert book sources into normalized documents."""

    def parse_text(self, title: str, content: str) -> Document:
        return Document(title=title, content=content)

    def split_chunks(self, document: Document, size: int = 500):
        text = document.content
        return [text[i:i + size] for i in range(0, len(text), size)]
