from celery import Celery
from celery import signature
from celery.events import EventReceiver
from celery.events.state import State


app_celery = None
state = State()

