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

class telegraf_general(client.BaseClient):
    """A client for interacting with the OPNSense's telegrafgeneral API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "telegraf/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "telegraf/general/set/"
        data = {}

        data = self._post( url, args)
        return data

class telegraf_input(client.BaseClient):
    """A client for interacting with the OPNSense's telegrafinput API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "telegraf/input/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "telegraf/input/set/"
        data = {}

        data = self._post( url, args)
        return data

class telegraf_key(client.BaseClient):
    """A client for interacting with the OPNSense's telegrafkey API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net-mgmt/telegraf/src/opnsense/mvc/app/models/OPNsense/Telegraf/Key.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addKey(self, args={}, params={}):
        """"""
        url = "telegraf/key/addKey/"
        data = {}

        data = self._post( url, args)
        return data

    def delKey(self, args={}, params={}):
        """"""
        url = "telegraf/key/delKey/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "telegraf/key/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getKey(self, args={}, params={}):
        """"""
        url = "telegraf/key/getKey/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchKey(self, args={}, params={}):
        """"""
        url = "telegraf/key/searchKey/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "telegraf/key/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setKey(self, args={}, params={}):
        """"""
        url = "telegraf/key/setKey/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleKey(self, args={}, params={}):
        """"""
        url = "telegraf/key/toggleKey/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class telegraf_output(client.BaseClient):
    """A client for interacting with the OPNSense's telegrafoutput API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "telegraf/output/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "telegraf/output/set/"
        data = {}

        data = self._post( url, args)
        return data

class telegraf_service(client.BaseClient):
    """A client for interacting with the OPNSense's telegrafservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "telegraf/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "telegraf/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "telegraf/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "telegraf/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "telegraf/service/stop/"
        data = {}

        data = self._post( url, args)
        return data
