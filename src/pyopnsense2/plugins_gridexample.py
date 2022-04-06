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

class gridexample_settings(client.BaseClient):
    """A client for interacting with the OPNSense's gridexamplesettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/devel/grid_example/src/opnsense/mvc/app/models/OPNsense/GridExample/GridExample.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addItem(self, args={}, params={}):
        """"""
        url = "gridexample/settings/addItem/"
        data = {}

        data = self._post( url, args)
        return data

    def delItem(self, args={}, params={}):
        """"""
        url = "gridexample/settings/delItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "gridexample/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getItem(self, args={}, params={}):
        """"""
        url = "gridexample/settings/getItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchItem(self, args={}, params={}):
        """"""
        url = "gridexample/settings/searchItem/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "gridexample/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setItem(self, args={}, params={}):
        """"""
        url = "gridexample/settings/setItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleItem(self, args={}, params={}):
        """"""
        url = "gridexample/settings/toggleItem/"
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
