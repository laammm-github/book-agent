"""Concept extraction utilities."""

from dataclasses import dataclass

from .pipeline import KnowledgeObject


@dataclass
class ConceptSet:
    title: str
    concepts: list[str]


class ConceptExtractor:
    """Extract key concepts from normalized book knowledge.

    Placeholder implementation for future LLM/NLP extraction.
    """

    def extract(self, knowledge: KnowledgeObject) -> ConceptSet:
        words = []
        for chunk in knowledge.chunks:
            for word in chunk.split():
                word = word.strip('.,!?()[]')
                if len(word) > 6 and word not in words:
                    words.append(word)
        return ConceptSet(
            title=knowledge.title,
            concepts=words[:20],
        )
