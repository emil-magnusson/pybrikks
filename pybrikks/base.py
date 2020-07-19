# -*- coding: utf-8 -*-

"""
brikksapi.base
"""

import json
import requests


class APIKeyError(Exception):
    pass


class URIKeyError(Exception):
    pass


class BRIKKS(object):

    def __init__(self):
        from . import BASE_URI
        if not BASE_URI:
            raise URIKeyError
        self.base_uri = BASE_URI
        self.headers = {
            "Content-Type": "charset=utf-8",
            "Accept": "application/json"
        }

    def _get_path(self, key):
        return self.BASE_PATH + self.URLS[key]

    def _get_id_path(self, key):
        return self._get_path(key).format(id=self.id)

    def _get_complete_url(self, path):
        return '{base_uri}/{path}'.format(base_uri=self.base_uri, path=path)

    def _set_header(self):
        from . import API_KEY
        if not API_KEY:
            raise APIKeyError
        self.headers.update({'Authorization': 'Bearer {}'.format(API_KEY)})

    def _request(self, method, path, params=None, payload=None):
        url = self._get_complete_url(path)
        self._set_header()

        response = requests.request(
            method, url, params=params,
            data=json.dumps(payload) if payload else payload,
            headers=self.headers)

        response.raise_for_status()
        return response.json()

    def _GET(self, path, params=None):
        return self._request('GET', path, params=params)
