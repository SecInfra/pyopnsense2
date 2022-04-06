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

class proxyuseracl_settings(client.BaseClient):
    """A client for interacting with the OPNSense's proxyuseraclsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/www/web-proxy-useracl/src/opnsense/mvc/app/models/OPNsense/ProxyUserACL/ProxyUserACL.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addACL(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/addACL/"
        data = {}

        data = self._post( url, args)
        return data

    def delACL(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/delACL/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getACL(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/getACL/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchACL(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/searchACL/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setACL(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/setACL/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def updownACL(self, args={}, params={}):
        """"""
        url = "proxyuseracl/settings/updownACL/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
