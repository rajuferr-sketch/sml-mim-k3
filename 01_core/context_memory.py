"""Shared context memory across all swarm agents."""
from typing import Dict, Any, List

class ContextMemory:
    def __init__(self):
        self._store: Dict[str, Any] = {}
        self._history: List[Dict[str, Any]] = []

    def set(self, key: str, value: Any):
        self._store[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._store.get(key, default)

    def log_event(self, agent_id: str, action: str, output: Any):
        self._history.append({"agent": agent_id, "action": action, "output": output})

    def get_history(self) -> List[Dict[str, Any]]:
        return self._history
