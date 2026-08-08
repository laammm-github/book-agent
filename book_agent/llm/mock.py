from .provider import LLMProvider


class MockLLMProvider(LLMProvider):
    """Offline provider for runtime tests."""

    def chat(self, messages, **kwargs):
        return "mock chat response"

    def complete(self, prompt, **kwargs):
        return "mock completion"

    def stream(self, messages, **kwargs):
        yield "mock stream"
