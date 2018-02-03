
import redis

import logging

from notifyme.config import config

logger = logging.getLogger(__name__)

session = None

POOL = None

def init_session():
    global session
    
    if session is None:
        session = redis.Redis(connection_pool=POOL)

def init_db_if_needed():
    global POOL
    global session

    if POOL is None:
        POOL = redis.ConnectionPool(
            host=config['REDIS_HOST'], 
            port=config['REDIS_PORT'],
            db=config['REDIS_DB']
        )
    
    if session is None:
        session = redis.Redis(connection_pool=POOL)


