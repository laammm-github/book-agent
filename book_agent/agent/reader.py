from .base import BaseAgent
from ..prompts.reader import build_reader_prompt


class ReaderAgent(BaseAgent):
    """Book comprehension and Q&A agent."""

    def __init__(self, llm_client=None):
        super().__init__("reader")
        self.llm_client = llm_client

    def run(self, task: str, context=None):
        book = getattr(context, "book", None)
        prompt = build_reader_prompt(task, book)

        if self.llm_client:
            response = self.llm_client.generate(prompt)
        else:
            response = "LLM client is not configured"

        return {
            "agent": self.name,
            "task": task,
            "book": book,
            "prompt": prompt,
            "response": response,
        }
