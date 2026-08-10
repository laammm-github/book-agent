from book_agent.agent.runtime import AgentRuntime


class DemoAgent:
    name = "demo"

    def run(self, task, context):
        return {"task": task, "context": context}


def test_runtime_initializes_and_runs():
    runtime = AgentRuntime()
    result = runtime.run("read chapter")
    assert runtime.lifecycle.is_running()
    assert result is not None


def test_runtime_register_and_run_agent():
    runtime = AgentRuntime()
    runtime.register(DemoAgent())

    result = runtime.run("read chapter", agent_name="demo")

    assert result["task"] == "read chapter"


def test_runtime_lifecycle_start():
    runtime = AgentRuntime()

    assert runtime.lifecycle.is_running() is False

    runtime.start()

    assert runtime.lifecycle.is_running() is True
