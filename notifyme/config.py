import os
import logging

logger = logging.getLogger(__name__)

config = {
    'ENVIRONMENT': 'Dev',
    'LOG_LEVEL': 'DEBUG',

    # No auth required
    'AUTH': False,

    # database part
    'REDIS_HOST': 'localhost',
    'REDIS_PORT': 6379,
    'REDIS_DB': 0,

    'SUBSCRIPTION_TYPE': [
        'ALWAYS',
        'ALL_TIME_LOW',
        'MORE_THAN_10',
    ],

    # tasks
    'BROKER_URL': 'redis://localhost:6379/0',

    'VERSION': '0.0.0'
}

