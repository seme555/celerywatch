from textual.screen import ModalScreen
from textual.widgets import Input, Button
from textual.containers import Grid

class CustomRetryModalScreen(ModalScreen[list]):
    def compose(self):
        yield Grid(
            Input(placeholder="Args: arg1, arg2", id="args"),
            Input(placeholder="Kwargs: a=1, b=2", id="kwargs"),
