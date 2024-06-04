from dataclasses import dataclass
from datetime import datetime

from rich.text import Text

@dataclass
class Task:
    uuid: str
    name: str
    args: str
    kwargs: str
    state: str
    styled_state: str
    exception: str
    styled_exception: str 
    traceback: str
    styled_traceback: str
    eta: str
    timestamp: str

@dataclass
class RetriableTask:
    uuid: str
    name: str
    args: str
    kwargs: str



class TaskRepository:
    def __init__(self):
        self._tasks: dict[str, Task] = {}
        self._tracebacks: dict[str, str] = {}
        self._retriable_tasks: dict[str, RetriableTask] = {}

    def add(self, task: Task):
        self._tasks[task.uuid] = task

    def add_traceback(self, key: str, traceback: str) -> None:
        self._tracebacks[key] = traceback

    def get_traceback(self, key: str) -> str | None:
        traceback = self._tracebacks.get(key)
        return traceback
    
    def add_retriable_task(self, task: Task) -> None:
        self._retriable_tasks[task.uuid] = RetriableTask(
            uuid=task.uuid,
