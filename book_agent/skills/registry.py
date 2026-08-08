"""Skill registration and discovery support."""

from typing import Dict, Type

from .skill import Skill


class SkillRegistry:
    """Registry for agent skills."""

    def __init__(self) -> None:
        self._skills: Dict[str, Type[Skill]] = {}

    def register(self, skill: Type[Skill]) -> None:
        self._skills[skill.name] = skill

    def get(self, name: str) -> Type[Skill] | None:
        return self._skills.get(name)

    def list_skills(self) -> list[str]:
        return list(self._skills.keys())
