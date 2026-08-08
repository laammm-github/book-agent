"""Embedding abstraction."""

from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):
    @abstractmethod
    def embed(self, text: str):
        raise NotImplementedError


class SimpleEmbeddingProvider(EmbeddingProvider):
    def embed(self, text: str):
        return [float(ord(c) % 100) / 100 for c in text[:16]]
