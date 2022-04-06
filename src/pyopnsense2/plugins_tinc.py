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

class tinc_service(client.BaseClient):
    """A client for interacting with the OPNSense's tincservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "tinc/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "tinc/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "tinc/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "tinc/service/stop/"
        data = {}

        data = self._post( url, args)
        return data

class tinc_settings(client.BaseClient):
    """A client for interacting with the OPNSense's tincsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/tinc/src/opnsense/mvc/app/models/OPNsense/Tinc/Tinc.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def delHost(self, args={}, params={}):
        """"""
        url = "tinc/settings/delHost/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delNetwork(self, args={}, params={}):
        """"""
        url = "tinc/settings/delNetwork/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "tinc/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getHost(self, args={}, params={}):
        """"""
        url = "tinc/settings/getHost/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getNetwork(self, args={}, params={}):
        """"""
        url = "tinc/settings/getNetwork/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchHost(self, args={}, params={}):
        """"""
        url = "tinc/settings/searchHost/"
        data = {}

        data = self._get( url, args)
        return data

    def searchNetwork(self, args={}, params={}):
        """"""
        url = "tinc/settings/searchNetwork/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "tinc/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setHost(self, args={}, params={}):
        """"""
        url = "tinc/settings/setHost/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setNetwork(self, args={}, params={}):
        """"""
        url = "tinc/settings/setNetwork/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleHost(self, args={}, params={}):
        """"""
        url = "tinc/settings/toggleHost/"
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

    def toggleNetwork(self, args={}, params={}):
        """"""
        url = "tinc/settings/toggleNetwork/"
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
