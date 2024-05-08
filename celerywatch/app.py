import ast
import asyncio

from textual.app import App
from textual.binding import Binding
from textual.widgets import DataTable, Header, Footer, Log
from textual.widgets._data_table import RowDoesNotExist
from celerywatch.broker import retry_task
from celerywatch.widgets import CustomRetryModalScreen
from celerywatch.models import TaskRepository
from celerywatch.utils import convert_args_safely


class CeleryMonitor(App):
    CSS_PATH = "styles/styles.tcss"

    BINDINGS = [
        Binding(key="r", action="", description="Retry Selected Task"),
        Binding(key="ctrl+r", action="custom_task_retry", description="Retry with custom args"),
        Binding(key='c', action='clear_table', description="Clear table data"),
        Binding(key="q", action="quit", description="Quit the app"),
