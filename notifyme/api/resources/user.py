import falcon
import logging

import notifyme.database.core as db
import notifyme.api.schemas as s

from notifyme.api.common import load_json_as_params

logger = logging.getLogger(__name__)

class User:
    
    @falcon.before(load_json_as_params)
    def on_post(self, req, resp, jdata):
        user_id = jdata.get('user_id')
        user_name = jdata.get('name')

        if not user_id or not user_name:
            raise falcon.HTTPBadRequest('Bad Request', 'Missing data')

        db.session.set(user_id, user_name)

    @falcon.before(load_json_as_params)
    def on_get(self, req, resp, jdata):
        user_id = jdata.get('user_id')

        if user_id is None:
            raise falcon.HTTPBadRequest('Bad Request', 'User not found')

        user = db.session.get(user_id)

        resp.body = user
        resp.status = falcon.HTTP_200

