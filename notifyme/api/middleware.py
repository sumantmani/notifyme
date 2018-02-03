import falcon
import logging

from notifyme.config import config

logger = logging.getLogger(__name__)

import notifyme.api.auth as au
from notifyme.config import config


class MyMiddleware(object):
    def process_request(self, req, resp):
        """Process the request before routing it."""
        self.cors_middleware(req, resp)
        if config.get('AUTH_ON'):
            au.auth(req, resp)

    def process_resource(self, req, resp, resource, params):
        """Process the request after routing."""
        pass

    def process_response(self, req, resp, resource, req_succeeded):
        """Post-processing of the response (after routing)."""
        pass

    def cors_middleware(self, req, resp):
        headers = []

        allowed_origins = map(
            lambda x: x.lstrip().rstrip(),
            filter(None, config.get('ALLOWED_ORIGIN', '').split(';'))
        )

        auth_header = config.get('HTTP_AUTH_HEADER', '')
        allowed_headers = 'Content-Type, {}'.format(auth_header)

        # origin = req.get_header('Origin')
        # logger.info('Origin :' + str(origin))

        # headers.append(('Access-Control-Allow-Credentials', 'true'))

        headers.append(('Access-Control-Allow-Headers', allowed_headers))
        headers.append(
            ('Access-Control-Allow-Methods', 'POST'))
        #headers.append(('Access-Control-Allow-Expose-Headers', auth_header))

        headers.append(('api-version', config['VERSION']))

        resp.set_headers(headers)

