from celery import Celery
from celery import signature
from celery.events import EventReceiver
from celery.events.state import State


app_celery = None
state = State()

def set_broker_uri(uri):
    global app_celery
    app_celery = Celery('celerywatch', broker=uri)

def retry_task(task_name, args=None, kwargs=None, broker_uri=None):
    global app_celery
    if app_celery is None:
        if broker_uri is None:
            raise RuntimeError("Celery app is not initialized and no broker URI was provided.")
