import falcon

import logging
logger = logging.getLogger(__name__)

class Root(object):

    def on_get(self, req, resp):
        resp.body = 'Awesome Notifyme API'
        resp.status = falcon.HTTP_200


