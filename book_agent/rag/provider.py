"""RAG provider integration abstractions."""

from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):
    """Interface for text embedding providers."""

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        raise NotImplementedError


class SimpleEmbeddingProvider(EmbeddingProvider):
    """Deterministic lightweight embedding for development and tests."""

    def embed(self, text: str) -> list[float]:
        value = float(len(text))
        return [value, value % 10, 1.0]
