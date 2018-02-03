import logging

from .core import app

logger = logging.getLogger(__name__)


@app.task
def notify(product_id, url, old_price, new_price, all_time_low, subscriber_list):

    for user_id, when in subscriber_list:
        if when == 'ALWAYS':
            logger.info('Notifyng user_id:' + user_id)
        if when == 'ALL_TIME_LOW' and all_time_low == True:
            logger.info('Notifying user_id:' + user_id)
        if when == 'MORE_THAN_10':
            logger.info('Nofigying user_id:' + user_id)


    logger.info('Sending notification:')




