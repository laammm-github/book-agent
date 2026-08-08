"""LLM provider abstraction for Book Agent."""

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def chat(self, prompt: str) -> str:
        raise NotImplementedError


class MockLLMProvider(LLMProvider):
    """Offline provider used for development and tests."""

    def chat(self, prompt: str) -> str:
        return f"Book Agent response: {prompt}"
