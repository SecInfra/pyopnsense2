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

class routes_gateway(client.BaseClient):
    """A client for interacting with the OPNSense's routesgateway API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def status(self, args={}, params={}):
        """"""
        url = "routes/gateway/status/"
        data = {}

        data = self._get( url, args)
        return data

class routes_routes(client.BaseClient):
    """A client for interacting with the OPNSense's routesroutes API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Routes/Route.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addroute(self, args={}, params={}):
        """"""
        url = "routes/routes/addroute/"
        data = {}

        data = self._post( url, args)
        return data

    def delroute(self, args={}, params={}):
        """"""
        url = "routes/routes/delroute/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "routes/routes/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getroute(self, args={}, params={}):
        """"""
        url = "routes/routes/getroute/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "routes/routes/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def searchroute(self, args={}, params={}):
        """"""
        url = "routes/routes/searchroute/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "routes/routes/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setroute(self, args={}, params={}):
        """"""
        url = "routes/routes/setroute/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleroute(self, args={}, params={}):
        """"""
        url = "routes/routes/toggleroute/"
        data = {}

        if "disabled" not in args.keys():
            return self.log_error("mandatory argument disabled is missing")
        else:
            url += args.pop("disabled")+"/"

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
