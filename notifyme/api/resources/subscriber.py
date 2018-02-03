
import logging

import falcon

import notifyme.api.schemas as s
import notifyme.database.core as db

from notifyme.api.common import load_json_as_params

logger = logging.getLogger(__name__)

class Subscriber:

    @falcon.before(load_json_as_params)
    def on_post(self, req, resp, jdata):
        # Validate input
        user_id = jdata.get('user_id')
        subscribe = jdata.get('subscribe')

        # may be a async task
        # Assuming everything work fine.
        for p in subscribe:
            product_id = p.get('product_id')
            when = p.get('when')

            product = db.session.get(product_id)
            product['subscriber_list'].add({
                'user_id':user_id, 
                'when': when
            })
            db.session.set(product_id, product)

        resp.status = falcon.HTTP_200

