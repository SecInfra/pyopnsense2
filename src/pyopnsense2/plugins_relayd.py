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

class relayd_service(client.BaseClient):
    """A client for interacting with the OPNSense's relaydservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/relayd/src/opnsense/mvc/app/models/OPNsense/Relayd/Relayd.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def configtest(self, args={}, params={}):
        """"""
        url = "relayd/service/configtest/"
        data = {}

        data = self._post( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "relayd/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "relayd/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "relayd/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "relayd/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "relayd/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

class relayd_settings(client.BaseClient):
    """A client for interacting with the OPNSense's relaydsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/relayd/src/opnsense/mvc/app/models/OPNsense/Relayd/Relayd.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def del(self, args={}, params={}):
        """"""
        url = "relayd/settings/del/"
        data = {}

        if "nodeType" not in args.keys():
            return self.log_error("mandatory argument nodeType is missing")
        else:
            url += args.pop("nodeType")+"/"

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def dirty(self, args={}, params={}):
        """"""
        url = "relayd/settings/dirty/"
        data = {}

        data = self._get( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "relayd/settings/get/"
        data = {}

        if "nodeType" not in args.keys():
            return self.log_error("mandatory argument nodeType is missing")
        else:
            url += args.pop("nodeType")+"/"

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def search(self, args={}, params={}):
        """"""
        url = "relayd/settings/search/"
        data = {}

        if "nodeType" not in args.keys():
            return self.log_error("mandatory argument nodeType is missing")
        else:
            url += args.pop("nodeType")+"/"

        data = self._post( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "relayd/settings/set/"
        data = {}

        if "nodeType" not in args.keys():
            return self.log_error("mandatory argument nodeType is missing")
        else:
            url += args.pop("nodeType")+"/"

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class relayd_status(client.BaseClient):
    """A client for interacting with the OPNSense's relaydstatus API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def sum(self, args={}, params={}):
        """"""
        url = "relayd/status/sum/"
        data = {}

        data = self._get( url, args)
        return data

    def toggle(self, args={}, params={}):
        """"""
        url = "relayd/status/toggle/"
        data = {}

        if "action" not in args.keys():
            return self.log_error("mandatory argument action is missing")
        else:
            url += args.pop("action")+"/"

        if "id" not in args.keys():
            return self.log_error("mandatory argument id is missing")
        else:
            url += args.pop("id")+"/"

        if "nodeType" not in args.keys():
            return self.log_error("mandatory argument nodeType is missing")
        else:
            url += args.pop("nodeType")+"/"

        data = self._post( url, args)
        return data
