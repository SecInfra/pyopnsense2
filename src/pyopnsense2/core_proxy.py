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

class proxy_service(client.BaseClient):
    """A client for interacting with the OPNSense's proxyservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Proxy/Proxy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def downloadacls(self, args={}, params={}):
        """"""
        url = "proxy/service/downloadacls/"
        data = {}

        data = self._post( url, args)
        return data

    def fetchacls(self, args={}, params={}):
        """"""
        url = "proxy/service/fetchacls/"
        data = {}

        data = self._post( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "proxy/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def refreshTemplate(self, args={}, params={}):
        """"""
        url = "proxy/service/refreshTemplate/"
        data = {}

        data = self._post( url, args)
        return data

    def reset(self, args={}, params={}):
        """"""
        url = "proxy/service/reset/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "proxy/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "proxy/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "proxy/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "proxy/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

class proxy_settings(client.BaseClient):
    """A client for interacting with the OPNSense's proxysettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Proxy/Proxy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addPACMatch(self, args={}, params={}):
        """"""
        url = "proxy/settings/addPACMatch/"
        data = {}

        data = self._post( url, args)
        return data

    def addPACProxy(self, args={}, params={}):
        """"""
        url = "proxy/settings/addPACProxy/"
        data = {}

        data = self._post( url, args)
        return data

    def addPACRule(self, args={}, params={}):
        """"""
        url = "proxy/settings/addPACRule/"
        data = {}

        data = self._post( url, args)
        return data

    def addRemoteBlacklist(self, args={}, params={}):
        """"""
        url = "proxy/settings/addRemoteBlacklist/"
        data = {}

        data = self._post( url, args)
        return data

    def delPACMatch(self, args={}, params={}):
        """"""
        url = "proxy/settings/delPACMatch/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delPACProxy(self, args={}, params={}):
        """"""
        url = "proxy/settings/delPACProxy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delPACRule(self, args={}, params={}):
        """"""
        url = "proxy/settings/delPACRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delRemoteBlacklist(self, args={}, params={}):
        """"""
        url = "proxy/settings/delRemoteBlacklist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def fetchRBCron(self, args={}, params={}):
        """"""
        url = "proxy/settings/fetchRBCron/"
        data = {}

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "proxy/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getPACMatch(self, args={}, params={}):
        """"""
        url = "proxy/settings/getPACMatch/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getPACProxy(self, args={}, params={}):
        """"""
        url = "proxy/settings/getPACProxy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getPACRule(self, args={}, params={}):
        """"""
        url = "proxy/settings/getPACRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getRemoteBlacklist(self, args={}, params={}):
        """"""
        url = "proxy/settings/getRemoteBlacklist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchPACMatch(self, args={}, params={}):
        """"""
        url = "proxy/settings/searchPACMatch/"
        data = {}

        data = self._get( url, args)
        return data

    def searchPACProxy(self, args={}, params={}):
        """"""
        url = "proxy/settings/searchPACProxy/"
        data = {}

        data = self._get( url, args)
        return data

    def searchPACRule(self, args={}, params={}):
        """"""
        url = "proxy/settings/searchPACRule/"
        data = {}

        data = self._get( url, args)
        return data

    def searchRemoteBlacklists(self, args={}, params={}):
        """"""
        url = "proxy/settings/searchRemoteBlacklists/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "proxy/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setPACMatch(self, args={}, params={}):
        """"""
        url = "proxy/settings/setPACMatch/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setPACProxy(self, args={}, params={}):
        """"""
        url = "proxy/settings/setPACProxy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setPACRule(self, args={}, params={}):
        """"""
        url = "proxy/settings/setPACRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setRemoteBlacklist(self, args={}, params={}):
        """"""
        url = "proxy/settings/setRemoteBlacklist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def togglePACRule(self, args={}, params={}):
        """"""
        url = "proxy/settings/togglePACRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRemoteBlacklist(self, args={}, params={}):
        """"""
        url = "proxy/settings/toggleRemoteBlacklist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class proxy_template(client.BaseClient):
    """A client for interacting with the OPNSense's proxytemplate API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Proxy/Proxy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "proxy/template/get/"
        data = {}

        data = self._get( url, args)
        return data

    def reset(self, args={}, params={}):
        """"""
        url = "proxy/template/reset/"
        data = {}

        data = self._post( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "proxy/template/set/"
        data = {}

        data = self._get( url, args)
        return data
