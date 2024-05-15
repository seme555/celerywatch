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
    ]

    def __init__(self, task_queue, broker_uri=None, **kwargs):
        super().__init__(**kwargs)
        self.task_queue = task_queue
        self.broker_uri = broker_uri
        self.added_tasks = set()
        self.title = "CeleryWatch - Debug and Monitor your celery tasks"
        self.task_repo = TaskRepository()

    def compose(self):
        yield Header(show_clock=True)
        self.table = DataTable(classes="table-outline")
        self.table.add_columns("UUID", "Name", "Args", "Kwargs", "State", "Datetime", "ETA")
        self.table.add_column("Exception", width=20)
        self.table.add_column("Traceback", width=20)
        self.table.cursor_type = 'row'
        self.table.zebra_stripes = True
        yield self.table

        self.traceback_panel = Log(highlight=True, classes="outline")
        self.traceback_panel.styles.height = 15
        self.traceback_panel.styles.dock = "bottom"
        self.traceback_panel.styles.margin = (0, 0, 1, 0)
        self.traceback_panel.styles.padding = 1
        self.traceback_panel.write("No traceback available")
        yield self.traceback_panel 

        yield Footer()

    async def on_mount(self):
        self.theme = "dracula"
        self.tracebacks = {}
        asyncio.create_task(self.update_table())

    async def create_retry_task_with_custom_args(self, action, r, k) -> None:
        if action:
            r, k = convert_args_safely(r, k)
            row_key = self.table.cursor_row
            if row_key is not None:
                try:
                    row = self.table.get_row_at(row_key)
                    uuid = row[0]
                    task = self.task_repo.get_retriable_task(uuid)
                    await self.retry_selected_task(
