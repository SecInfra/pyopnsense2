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

class trafficshaper_service(client.BaseClient):
    """A client for interacting with the OPNSense's trafficshaperservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def flushreload(self, args={}, params={}):
        """"""
        url = "trafficshaper/service/flushreload/"
        data = {}

        data = self._post( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "trafficshaper/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def statistics(self, args={}, params={}):
        """"""
        url = "trafficshaper/service/statistics/"
        data = {}

        data = self._get( url, args)
        return data

class trafficshaper_settings(client.BaseClient):
    """A client for interacting with the OPNSense's trafficshapersettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/TrafficShaper/TrafficShaper.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addPipe(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/addPipe/"
        data = {}

        data = self._post( url, args)
        return data

    def addQueue(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/addQueue/"
        data = {}

        data = self._post( url, args)
        return data

    def addRule(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/addRule/"
        data = {}

        data = self._post( url, args)
        return data

    def delPipe(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/delPipe/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delQueue(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/delQueue/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delRule(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/delRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getPipe(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/getPipe/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getQueue(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/getQueue/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getRule(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/getRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchPipes(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/searchPipes/"
        data = {}

        data = self._get( url, args)
        return data

    def searchQueues(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/searchQueues/"
        data = {}

        data = self._get( url, args)
        return data

    def searchRules(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/searchRules/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setPipe(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/setPipe/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setQueue(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/setQueue/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setRule(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/setRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def togglePipe(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/togglePipe/"
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

    def toggleQueue(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/toggleQueue/"
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

    def toggleRule(self, args={}, params={}):
        """"""
        url = "trafficshaper/settings/toggleRule/"
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
