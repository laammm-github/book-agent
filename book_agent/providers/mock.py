from .base import BaseLLMProvider


class MockLLMProvider(BaseLLMProvider):
    """Local provider for development and testing."""

    def generate(self, prompt: str) -> str:
        return (
            "Mock Book Agent Response\n\n"
            f"Question: {prompt}\n\n"
            "Key points:\n"
            "1. Extract core ideas\n"
            "2. Connect concepts\n"
            "3. Provide reflection questions"
        )
