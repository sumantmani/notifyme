
import logging

import falcon

import notifyme.api.schemas as s
import notifyme.database.core as db

from notifyme.api.common import load_json_as_params

logger = logging.getLogger(__name__)

class Unsubscriber:
    def __init__(self):
        self.name = 'Subscriber'

    @falcon.before(load_json_as_params)
    def on_post(self, req, resp, jdata):
        # Validate input
        user_id = jdata.get('user_id')
        unsubscribe = jdata.get('unsubscribe')
        
        for product_id in unsubscribe:
            product = db.session.get(product_id)
            product['subscriber_list'].remove(user_id) # TODO: need to fix it.
            db.session.set(product_id, product) # This is bad.
            
        resp.status = falcon.HTTP_200


