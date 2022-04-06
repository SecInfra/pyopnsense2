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

class clamav_general(client.BaseClient):
    """A client for interacting with the OPNSense's clamavgeneral API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/clamav/src/opnsense/mvc/app/models/OPNsense/ClamAV/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "clamav/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "clamav/general/set/"
        data = {}

        data = self._get( url, args)
        return data

class clamav_service(client.BaseClient):
    """A client for interacting with the OPNSense's clamavservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/clamav/src/opnsense/mvc/app/models/OPNsense/ClamAV/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def freshclam(self, args={}, params={}):
        """"""
        url = "clamav/service/freshclam/"
        data = {}

        data = self._post( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "clamav/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "clamav/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "clamav/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "clamav/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "clamav/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

    def version(self, args={}, params={}):
        """"""
        url = "clamav/service/version/"
        data = {}

        data = self._get( url, args)
        return data

class clamav_url(client.BaseClient):
    """A client for interacting with the OPNSense's clamavurl API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/clamav/src/opnsense/mvc/app/models/OPNsense/ClamAV/Url.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addUrl(self, args={}, params={}):
        """"""
        url = "clamav/url/addUrl/"
        data = {}

        data = self._post( url, args)
        return data

    def delUrl(self, args={}, params={}):
        """"""
        url = "clamav/url/delUrl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "clamav/url/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getUrl(self, args={}, params={}):
        """"""
        url = "clamav/url/getUrl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchUrl(self, args={}, params={}):
        """"""
        url = "clamav/url/searchUrl/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "clamav/url/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setUrl(self, args={}, params={}):
        """"""
        url = "clamav/url/setUrl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleUrl(self, args={}, params={}):
        """"""
        url = "clamav/url/toggleUrl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
