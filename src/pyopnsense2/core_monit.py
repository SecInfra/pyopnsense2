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

class monit_service(client.BaseClient):
    """A client for interacting with the OPNSense's monitservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Monit/Monit.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def configtest(self, args={}, params={}):
        """"""
        url = "monit/service/configtest/"
        data = {}

        data = self._post( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "monit/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "monit/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "monit/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "monit/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "monit/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

class monit_settings(client.BaseClient):
    """A client for interacting with the OPNSense's monitsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Monit/Monit.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addAlert(self, args={}, params={}):
        """"""
        url = "monit/settings/addAlert/"
        data = {}

        data = self._post( url, args)
        return data

    def addService(self, args={}, params={}):
        """"""
        url = "monit/settings/addService/"
        data = {}

        data = self._post( url, args)
        return data

    def addTest(self, args={}, params={}):
        """"""
        url = "monit/settings/addTest/"
        data = {}

        data = self._post( url, args)
        return data

    def delAlert(self, args={}, params={}):
        """"""
        url = "monit/settings/delAlert/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delService(self, args={}, params={}):
        """"""
        url = "monit/settings/delService/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delTest(self, args={}, params={}):
        """"""
        url = "monit/settings/delTest/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def dirty(self, args={}, params={}):
        """"""
        url = "monit/settings/dirty/"
        data = {}

        data = self._get( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "monit/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAlert(self, args={}, params={}):
        """"""
        url = "monit/settings/getAlert/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getGeneral(self, args={}, params={}):
        """"""
        url = "monit/settings/getGeneral/"
        data = {}

        data = self._get( url, args)
        return data

    def getService(self, args={}, params={}):
        """"""
        url = "monit/settings/getService/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getTest(self, args={}, params={}):
        """"""
        url = "monit/settings/getTest/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchAlert(self, args={}, params={}):
        """"""
        url = "monit/settings/searchAlert/"
        data = {}

        data = self._get( url, args)
        return data

    def searchService(self, args={}, params={}):
        """"""
        url = "monit/settings/searchService/"
        data = {}

        data = self._get( url, args)
        return data

    def searchTest(self, args={}, params={}):
        """"""
        url = "monit/settings/searchTest/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "monit/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setAlert(self, args={}, params={}):
        """"""
        url = "monit/settings/setAlert/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setService(self, args={}, params={}):
        """"""
        url = "monit/settings/setService/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setTest(self, args={}, params={}):
        """"""
        url = "monit/settings/setTest/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleAlert(self, args={}, params={}):
        """"""
        url = "monit/settings/toggleAlert/"
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

    def toggleService(self, args={}, params={}):
        """"""
        url = "monit/settings/toggleService/"
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

class monit_status(client.BaseClient):
    """A client for interacting with the OPNSense's monitstatus API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "monit/status/get/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data
