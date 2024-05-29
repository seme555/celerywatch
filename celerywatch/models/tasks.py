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
