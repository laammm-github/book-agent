from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """Base interface for LLM providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
