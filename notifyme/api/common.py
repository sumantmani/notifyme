import ujson as json

import logging

import falcon

logger = logging.getLogger(__name__)


def load_json_as_params(req, resp, resource, params):
    try:
        data = json.load(req.bounded_stream)
    except ValueError:
        raise falcon.HTTPBadRequest('Bad Request', 'Missing data')

    params['jdata'] = data


def load_ident(req, resp, resource, params):
    params['ident'] = req.env.get('wsgi.identity')

