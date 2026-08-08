from .base import BaseAgent


class ReviewerAgent(BaseAgent):
    """Generate reading reviews and reflection questions."""

    def run(self, task: str):
        return {
            "type": "review",
            "task": task,
            "questions": [
                "这本书最重要的观点是什么？",
                "哪些内容改变了你的认知？",
            ],
        }
