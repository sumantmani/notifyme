import celery
import logging

from celery import Celery, Task
from datetime import timedelta

from notifyme.config import config

logger = logging.getLogger(__name__)

app = Celery(
    'notifyme-api-tasks',
    broker=config.get('BROKER_URL'),
    backend=config.get('BROKER_URL')
)

app.conf.beat_schedule = {
    'test-task': {
        'task': 'notifyme.api.tasks.core.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

app.conf.timezone = 'UTC'


@app.task
def add(x, y):
    logger.info('This is add fuction ')

