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

class stunnel_service(client.BaseClient):
    """A client for interacting with the OPNSense's stunnelservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/stunnel/src/opnsense/mvc/app/models/OPNsense/Stunnel/Stunnel.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "stunnel/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "stunnel/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "stunnel/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "stunnel/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "stunnel/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

class stunnel_services(client.BaseClient):
    """A client for interacting with the OPNSense's stunnelservices API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/stunnel/src/opnsense/mvc/app/models/OPNsense/Stunnel/Stunnel.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addItem(self, args={}, params={}):
        """"""
        url = "stunnel/services/addItem/"
        data = {}

        data = self._post( url, args)
        return data

    def delItem(self, args={}, params={}):
        """"""
        url = "stunnel/services/delItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "stunnel/services/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getItem(self, args={}, params={}):
        """"""
        url = "stunnel/services/getItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchItem(self, args={}, params={}):
        """"""
        url = "stunnel/services/searchItem/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "stunnel/services/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setItem(self, args={}, params={}):
        """"""
        url = "stunnel/services/setItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleItem(self, args={}, params={}):
        """"""
        url = "stunnel/services/toggleItem/"
        data = {}

        if "enabled" not in args.keys():
            return self.log_error("mandatory argument enabled is missing")
        else:
            url += args.pop("enabled")+"/"

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
