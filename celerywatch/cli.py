import argparse
import multiprocessing
from celerywatch.app import CeleryMonitor
from celerywatch.broker import event_worker

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--broker', required=True, help='Celery broker URI (e.g. redis://localhost:6379/0)')
    args = parser.parse_args()
