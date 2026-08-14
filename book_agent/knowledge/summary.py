"""Book summary generation utilities."""

from dataclasses import dataclass

from .pipeline import KnowledgeObject


@dataclass
class BookSummary:
    title: str
    summary: str


class SummaryGenerator:
    """Generate deterministic summaries from knowledge objects.

    This foundation keeps the interface ready for LLM powered summaries.
    """

    def generate(self, knowledge: KnowledgeObject) -> BookSummary:
        preview = " ".join(knowledge.chunks[:2])
        return BookSummary(
            title=knowledge.title,
            summary=preview,
        )
