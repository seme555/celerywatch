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
