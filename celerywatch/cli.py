import argparse
import multiprocessing
from celerywatch.app import CeleryMonitor
from celerywatch.broker import event_worker

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--broker', required=True, help='Celery broker URI (e.g. redis://localhost:6379/0)')
    args = parser.parse_args()

    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=event_worker, args=(queue, args.broker))
    p.start()
    try:
        CeleryMonitor(task_queue=queue, broker_uri=args.broker).run()
    finally:
        p.terminate()
        p.join()
