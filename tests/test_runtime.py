from book_agent.agent.runtime import AgentRuntime


def test_runtime_initializes_and_runs():
    runtime = AgentRuntime()
    result = runtime.run("read chapter")
    assert runtime.lifecycle.is_running()
    assert result is not None
