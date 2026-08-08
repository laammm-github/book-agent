"""Agent lifecycle state management."""

from enum import Enum


class AgentState(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    STOPPED = "stopped"


class LifecycleManager:
    def __init__(self):
        self.state = AgentState.CREATED

    def start(self):
        self.state = AgentState.RUNNING

    def stop(self):
        self.state = AgentState.STOPPED

    def is_running(self):
        return self.state == AgentState.RUNNING
