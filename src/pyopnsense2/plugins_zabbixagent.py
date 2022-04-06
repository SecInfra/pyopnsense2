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

class zabbixagent_service(client.BaseClient):
    """A client for interacting with the OPNSense's zabbixagentservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net-mgmt/zabbix-agent/src/opnsense/mvc/app/models/OPNsense/ZabbixAgent/ZabbixAgent.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "zabbixagent/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "zabbixagent/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "zabbixagent/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "zabbixagent/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "zabbixagent/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

class zabbixagent_settings(client.BaseClient):
    """A client for interacting with the OPNSense's zabbixagentsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net-mgmt/zabbix-agent/src/opnsense/mvc/app/models/OPNsense/ZabbixAgent/ZabbixAgent.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addAlias(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/addAlias/"
        data = {}

        data = self._post( url, args)
        return data

    def addUserparameter(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/addUserparameter/"
        data = {}

        data = self._post( url, args)
        return data

    def delAlias(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/delAlias/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delUserparameter(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/delUserparameter/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAlias(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/getAlias/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getUserparameter(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/getUserparameter/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchAliases(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/searchAliases/"
        data = {}

        data = self._get( url, args)
        return data

    def searchUserparameters(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/searchUserparameters/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setAlias(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/setAlias/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setUserparameter(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/setUserparameter/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleAlias(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/toggleAlias/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleUserparameter(self, args={}, params={}):
        """"""
        url = "zabbixagent/settings/toggleUserparameter/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
