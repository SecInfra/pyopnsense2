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

class ftpproxy_service(client.BaseClient):
    """A client for interacting with the OPNSense's ftpproxyservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def config(self, args={}, params={}):
        """"""
        url = "ftpproxy/service/config/"
        data = {}

        data = self._post( url, args)
        return data

    def reload(self, args={}, params={}):
        """"""
        url = "ftpproxy/service/reload/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "ftpproxy/service/restart/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "ftpproxy/service/start/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "ftpproxy/service/status/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "ftpproxy/service/stop/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class ftpproxy_settings(client.BaseClient):
    """A client for interacting with the OPNSense's ftpproxysettings API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addProxy(self, args={}, params={}):
        """"""
        url = "ftpproxy/settings/addProxy/"
        data = {}

        data = self._post( url, args)
        return data

    def delProxy(self, args={}, params={}):
        """"""
        url = "ftpproxy/settings/delProxy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def getProxy(self, args={}, params={}):
        """"""
        url = "ftpproxy/settings/getProxy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchProxy(self, args={}, params={}):
        """"""
        url = "ftpproxy/settings/searchProxy/"
        data = {}

        data = self._get( url, args)
        return data

    def setProxy(self, args={}, params={}):
        """"""
        url = "ftpproxy/settings/setProxy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleProxy(self, args={}, params={}):
        """"""
        url = "ftpproxy/settings/toggleProxy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
