from book_agent.agent.context import AgentContext
from book_agent.llm.mock import MockLLMProvider


def test_context_memory_hooks():
    context = AgentContext(session_id="s1", task="read")
    context.add_history("hello")
    assert context.history == ["hello"]


def test_mock_llm():
    provider = MockLLMProvider()
    assert provider.complete("x") == "mock completion"
    assert list(provider.stream([])) == ["mock stream"]
