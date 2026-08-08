"""CLI entry for Book Agent."""

from book_agent.agent.orchestrator import OrchestratorAgent


def main():
    agent = OrchestratorAgent()
    print(agent.run("start reading session"))


if __name__ == "__main__":
    main()
