from abc import ABC, abstractmethod
from typing import Iterable


class LLMProvider(ABC):
    """Abstract interface for language model providers."""

    @abstractmethod
    def chat(self, messages: list[dict[str, str]], **kwargs):
        raise NotImplementedError

    @abstractmethod
    def complete(self, prompt: str, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def stream(self, messages: list[dict[str, str]], **kwargs) -> Iterable[str]:
        raise NotImplementedError
