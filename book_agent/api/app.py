"""Book Agent API entrypoint."""


class BookAgentAPI:
    def __init__(self, agent):
        self.agent = agent

    def chat(self, message: str):
        return self.agent.run(message)
