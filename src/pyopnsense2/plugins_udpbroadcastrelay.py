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

class udpbroadcastrelay_service(client.BaseClient):
    """A client for interacting with the OPNSense's udpbroadcastrelayservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/udpbroadcastrelay/src/opnsense/mvc/app/models/OPNsense/UDPBroadcastRelay/UDPBroadcastRelay.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def config(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/config/"
        data = {}

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/get/"
        data = {}

        data = self._get( url, args)
        return data

    def reload(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/reload/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/restart/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/set/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/start/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/status/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/service/stop/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class udpbroadcastrelay_settings(client.BaseClient):
    """A client for interacting with the OPNSense's udpbroadcastrelaysettings API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addRelay(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/addRelay/"
        data = {}

        data = self._post( url, args)
        return data

    def delRelay(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/delRelay/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getRelay(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/getRelay/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchRelay(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/searchRelay/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setRelay(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/setRelay/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRelay(self, args={}, params={}):
        """"""
        url = "udpbroadcastrelay/settings/toggleRelay/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
