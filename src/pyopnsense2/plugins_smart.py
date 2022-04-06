#!/bin/python3
# Copyright 2021 by opensource@secinfra.fr
# Initially from Matthew Treinish's https://github.com/mtreinish/pyopnsense
# Improved a bit.

#
# This file is part of pyopnsense2
#
# pyopnsense2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyopnsense2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyopnsense2. If not, see <http://www.gnu.org/licenses/>.

from pyopnsense2 import client
from six.moves import urllib
import json

class smart_service(client.BaseClient):
    """A client for interacting with the OPNSense's smartservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def abort(self, args={}, params={}):
        """"""
        url = "smart/service/abort/"
        data = {}

        data = self._post( url, args)
        return data

    def info(self, args={}, params={}):
        """"""
        url = "smart/service/info/"
        data = {}

        data = self._post( url, args)
        return data

    def list(self, args={}, params={}):
        """"""
        url = "smart/service/list/"
        data = {}

        data = self._post( url, args)
        return data

    def logs(self, args={}, params={}):
        """"""
        url = "smart/service/logs/"
        data = {}

        data = self._post( url, args)
        return data

    def test(self, args={}, params={}):
        """"""
        url = "smart/service/test/"
        data = {}

        data = self._post( url, args)
        return data
