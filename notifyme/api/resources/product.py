
import logging

import falcon

import notifyme.api.schemas as s
import notifyme.database.core as db

from notifyme.api.common import load_json_as_params
from notifyme.api.tasks import notify

logger = logging.getLogger(__name__)

class Product:

    @falcon.before(load_json_as_params)
    def on_post(self, req, resp, jdata):
        # Validate input
        product_id = jdata.get('product_id')
        new_price = jdata.get('price')
        url = jdata.get('url')

        # async task
        product = db.session.get(product_id)
        if product:
            subscriber_list = product['subscriber_list']
            min_price = product['min_price']
            all_time_low = True if min_price < new_price else False

            # TODO @sumantmani: make it async
            notify(product_id, url, product['price'], new_price, all_time_low, subscriber_list)

            if all_time_low:
                product['min_price'] = price
            product['price'] = price
        else:
            # adding new product
            product = {
                'product_id': product_id,
                'price': price,
                'min_price': price,
                'url': url,
                'subscriber_list': [],
            }

        db.session.set(product_id, product)

        resp.status = falcon.HTTP_200



# Redundent
class AddProduct:
    @falcon.before(load_json_as_params)
    def on_post(self, req, resp, jdata):
        product_id = jdata.get('product_id')
        price = jdata.get('price')
        url = jdata.get('url')
        
        product = {
            'product_id': product_id,
            'price': price,
            'min_price': price,
            'url': url,
            'subscriber_list': [],
        }
        db.session.set(product_id, product)
        
        resp.body, errors = s.ProductSchema().dumps(product)
        resp.status = falcon.HTTP_200

