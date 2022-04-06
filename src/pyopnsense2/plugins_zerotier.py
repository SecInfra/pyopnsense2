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

class zerotier_network(client.BaseClient):
    """A client for interacting with the OPNSense's zerotiernetwork API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/zerotier/src/opnsense/mvc/app/models/OPNsense/Zerotier/Zerotier.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def add(self, args={}, params={}):
        """"""
        url = "zerotier/network/add/"
        data = {}

        data = self._post( url, args)
        return data

    def del(self, args={}, params={}):
        """"""
        url = "zerotier/network/del/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "zerotier/network/get/"
        data = {}

        data = self._get( url, args)
        return data

    def info(self, args={}, params={}):
        """"""
        url = "zerotier/network/info/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def search(self, args={}, params={}):
        """"""
        url = "zerotier/network/search/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "zerotier/network/set/"
        data = {}

        data = self._get( url, args)
        return data

    def toggle(self, args={}, params={}):
        """"""
        url = "zerotier/network/toggle/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class zerotier_settings(client.BaseClient):
    """A client for interacting with the OPNSense's zerotiersettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/zerotier/src/opnsense/mvc/app/models/OPNsense/Zerotier/Zerotier.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "zerotier/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "zerotier/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "zerotier/settings/status/"
        data = {}

        data = self._get( url, args)
        return data
