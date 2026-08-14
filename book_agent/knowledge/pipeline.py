"""Book understanding pipeline.

Connects loaders and parsers into a simple ingestion flow.
"""

from dataclasses import dataclass

from .parser import BookParser, Document


@dataclass
class KnowledgeObject:
    """Normalized knowledge unit generated from a book document."""

    title: str
    chunks: list[str]


class BookKnowledgePipeline:
    """Build normalized knowledge objects from book content."""

    def __init__(self, parser: BookParser | None = None):
        self.parser = parser or BookParser()

    def build(self, title: str, content: str) -> KnowledgeObject:
        document: Document = self.parser.parse_text(title, content)
        chunks = self.parser.split_chunks(document)

        return KnowledgeObject(
            title=document.title,
            chunks=chunks,
        )
