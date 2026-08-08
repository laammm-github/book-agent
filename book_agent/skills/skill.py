from abc import ABC, abstractmethod


class Skill(ABC):
    """Reusable capability unit for agents."""

    name = "skill"

    @abstractmethod
    def execute(self, input_data):
        pass


class SummarySkill(Skill):
    name = "summary"

    def execute(self, input_data):
        return f"Summary generated: {input_data}"
