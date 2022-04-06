# Copyright 2021 by opensource@secinfra.fr
# Initially from Matthew Treinish's https://github.com/mtreinish/pyopnsense
# Improved a bit.


import json

import requests
from requests.auth import HTTPDigestAuth

from pyopnsense2 import exceptions

DEFAULT_TIMEOUT = 5

# All the successful HTTP status codes from RFC 7231 & 4918
HTTP_SUCCESS = (200, 201, 202, 203, 204, 205, 206, 207)


class BaseClient(object):
    """Representation of the OPNsense API client."""

    def __init__(self, params={}):
        """Initialize the OPNsense API client."""
        self.params = params

    def log_error(self, msg):
        return { "error" : "[x] %s" % msg }

    def _process_response(self, response):
        """Handle the response."""
        if response.status_code in HTTP_SUCCESS:
            try:
                result = json.loads(response.text)
            except Exception as e:
                result = {'exception':str(e)}
        else:
            result = {'error': {
                "status_code": response.status_code, 
                "resp_body":response.text
            }}
        return result

    def format_url(self, endpoint):
        return '{}/{}'.format(self.params['base_url'], endpoint)

    def _get(self, endpoint, body="NO USE"):
        req_url = self.format_url(endpoint)
        response = requests.get(req_url, verify=self.params['verify_cert'],
                                auth=self.params['auth'],
                                timeout=self.params['timeout'])
        return self._process_response(response)

    def _post(self, endpoint, body):
        req_url = self.format_url(endpoint)
        response = requests.post(req_url, json=body,
                                 verify=self.params['verify_cert'],
                                 auth=self.params['auth'],
                                 timeout=self.params['timeout'])
        return self._process_response(response)
