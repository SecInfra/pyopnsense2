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

class wireguard_client(client.BaseClient):
    """A client for interacting with the OPNSense's wireguardclient API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/Client.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addClient(self, args={}, params={}):
        """"""
        url = "wireguard/client/addClient/"
        data = {}

        data = self._post( url, args)
        return data

    def delClient(self, args={}, params={}):
        """"""
        url = "wireguard/client/delClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "wireguard/client/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getClient(self, args={}, params={}):
        """"""
        url = "wireguard/client/getClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchClient(self, args={}, params={}):
        """"""
        url = "wireguard/client/searchClient/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "wireguard/client/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setClient(self, args={}, params={}):
        """"""
        url = "wireguard/client/setClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleClient(self, args={}, params={}):
        """"""
        url = "wireguard/client/toggleClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class wireguard_general(client.BaseClient):
    """A client for interacting with the OPNSense's wireguardgeneral API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "wireguard/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "wireguard/general/set/"
        data = {}

        data = self._get( url, args)
        return data

class wireguard_server(client.BaseClient):
    """A client for interacting with the OPNSense's wireguardserver API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/Server.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addServer(self, args={}, params={}):
        """"""
        url = "wireguard/server/addServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delServer(self, args={}, params={}):
        """"""
        url = "wireguard/server/delServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "wireguard/server/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getServer(self, args={}, params={}):
        """"""
        url = "wireguard/server/getServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchServer(self, args={}, params={}):
        """"""
        url = "wireguard/server/searchServer/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "wireguard/server/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setServer(self, args={}, params={}):
        """"""
        url = "wireguard/server/setServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleServer(self, args={}, params={}):
        """"""
        url = "wireguard/server/toggleServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class wireguard_service(client.BaseClient):
    """A client for interacting with the OPNSense's wireguardservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "wireguard/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "wireguard/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def showconf(self, args={}, params={}):
        """"""
        url = "wireguard/service/showconf/"
        data = {}

        data = self._get( url, args)
        return data

    def showhandshake(self, args={}, params={}):
        """"""
        url = "wireguard/service/showhandshake/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "wireguard/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "wireguard/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "wireguard/service/stop/"
        data = {}

        data = self._get( url, args)
        return data
