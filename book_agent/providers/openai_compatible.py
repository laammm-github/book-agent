"""OpenAI compatible LLM provider.

This module keeps the model layer replaceable for providers such as
OpenAI-compatible gateways, local models and cloud APIs.
"""

from dataclasses import dataclass
from typing import Iterable


@dataclass
class LLMResponse:
    text: str
    model: str = "mock"


class OpenAICompatibleProvider:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str = "default"):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model

    def chat(self, messages: list[dict[str, str]]) -> LLMResponse:
        """Generate a response.

        The network implementation is intentionally isolated so applications can
        inject their preferred SDK/client later.
        """
        content = messages[-1]["content"] if messages else ""
        return LLMResponse(text=f"Book Agent received: {content}", model=self.model)

    def stream(self, text: str) -> Iterable[str]:
        for token in text.split():
            yield token
