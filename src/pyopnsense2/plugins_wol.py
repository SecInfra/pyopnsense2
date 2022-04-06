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

class wol_wol(client.BaseClient):
    """A client for interacting with the OPNSense's wolwol API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/wol/src/opnsense/mvc/app/models/OPNsense/Wol/Wol.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addHost(self, args={}, params={}):
        """"""
        url = "wol/wol/addHost/"
        data = {}

        data = self._post( url, args)
        return data

    def delHost(self, args={}, params={}):
        """"""
        url = "wol/wol/delHost/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "wol/wol/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getHost(self, args={}, params={}):
        """"""
        url = "wol/wol/getHost/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getwake(self, args={}, params={}):
        """"""
        url = "wol/wol/getwake/"
        data = {}

        data = self._get( url, args)
        return data

    def searchHost(self, args={}, params={}):
        """"""
        url = "wol/wol/searchHost/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "wol/wol/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setHost(self, args={}, params={}):
        """"""
        url = "wol/wol/setHost/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def wakeall(self, args={}, params={}):
        """"""
        url = "wol/wol/wakeall/"
        data = {}

        data = self._post( url, args)
        return data
