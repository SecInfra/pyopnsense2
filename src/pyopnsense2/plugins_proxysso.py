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

class proxysso_service(client.BaseClient):
    """A client for interacting with the OPNSense's proxyssoservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def createkeytab(self, args={}, params={}):
        """"""
        url = "proxysso/service/createkeytab/"
        data = {}

        data = self._post( url, args)
        return data

    def deletekeytab(self, args={}, params={}):
        """"""
        url = "proxysso/service/deletekeytab/"
        data = {}

        data = self._get( url, args)
        return data

    def getCheckList(self, args={}, params={}):
        """"""
        url = "proxysso/service/getCheckList/"
        data = {}

        data = self._get( url, args)
        return data

    def showkeytab(self, args={}, params={}):
        """"""
        url = "proxysso/service/showkeytab/"
        data = {}

        data = self._get( url, args)
        return data

    def testkerblogin(self, args={}, params={}):
        """"""
        url = "proxysso/service/testkerblogin/"
        data = {}

        data = self._post( url, args)
        return data

class proxysso_settings(client.BaseClient):
    """A client for interacting with the OPNSense's proxyssosettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/www/web-proxy-sso/src/opnsense/mvc/app/models/OPNsense/ProxySSO/ProxySSO.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "proxysso/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "proxysso/settings/set/"
        data = {}

        data = self._get( url, args)
        return data
