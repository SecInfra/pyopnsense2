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

class collectd_general(client.BaseClient):
    """A client for interacting with the OPNSense's collectdgeneral API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "collectd/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "collectd/general/set/"
        data = {}

        data = self._post( url, args)
        return data

class collectd_service(client.BaseClient):
    """A client for interacting with the OPNSense's collectdservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "collectd/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "collectd/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "collectd/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "collectd/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "collectd/service/stop/"
        data = {}

        data = self._post( url, args)
        return data
