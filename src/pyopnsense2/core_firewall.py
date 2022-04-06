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

class firewall_alias(client.BaseClient):
    """A client for interacting with the OPNSense's firewallalias API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Alias.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addItem(self, args={}, params={}):
        """"""
        url = "firewall/alias/addItem/"
        data = {}

        data = self._post( url, args)
        return data

    def delItem(self, args={}, params={}):
        """"""
        url = "firewall/alias/delItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def export(self, args={}, params={}):
        """"""
        url = "firewall/alias/export/"
        data = {}

        data = self._get( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "firewall/alias/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAliasUUID(self, args={}, params={}):
        """"""
        url = "firewall/alias/getAliasUUID/"
        data = {}

        if "name" not in args.keys():
            return self.log_error("mandatory argument name is missing")
        else:
            url += args.pop("name")+"/"

        data = self._get( url, args)
        return data

    def getGeoIP(self, args={}, params={}):
        """"""
        url = "firewall/alias/getGeoIP/"
        data = {}

        data = self._get( url, args)
        return data

    def getItem(self, args={}, params={}):
        """"""
        url = "firewall/alias/getItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def doImport(self, args={}, params={}):
        """"""
        url = "firewall/alias/import/"
        data = {}

        data = self._post( url, args)
        return data

    def listCountries(self, args={}, params={}):
        """"""
        url = "firewall/alias/listCountries/"
        data = {}

        data = self._get( url, args)
        return data

    def listNetworkAliases(self, args={}, params={}):
        """"""
        url = "firewall/alias/listNetworkAliases/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "firewall/alias/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def searchItem(self, args={}, params={}):
        """"""
        url = "firewall/alias/searchItem/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "firewall/alias/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setItem(self, args={}, params={}):
        """"""
        url = "firewall/alias/setItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleItem(self, args={}, params={}):
        """"""
        url = "firewall/alias/toggleItem/"
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

class firewall_alias_util(client.BaseClient):
    """A client for interacting with the OPNSense's firewallalias_util API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def add(self, args={}, params={}):
        """"""
        url = "firewall/alias_util/add/"
        data = {}

        if "aliasName" not in args.keys():
            return self.log_error("mandatory argument aliasName is missing")
        else:
            url += args.pop("aliasName")+"/"

        data = self._post( url, args)
        return data

    def aliases(self, args={}, params={}):
        """"""
        url = "firewall/alias_util/aliases/"
        data = {}

        data = self._get( url, args)
        return data

    def delete(self, args={}, params={}):
        """"""
        url = "firewall/alias_util/delete/"
        data = {}

        if "aliasName" not in args.keys():
            return self.log_error("mandatory argument aliasName is missing")
        else:
            url += args.pop("aliasName")+"/"

        data = self._post( url, args)
        return data

    def find_references(self, args={}, params={}):
        """"""
        url = "firewall/alias_util/find_references/"
        data = {}

        data = self._post( url, args)
        return data

    def flush(self, args={}, params={}):
        """"""
        url = "firewall/alias_util/flush/"
        data = {}

        if "aliasName" not in args.keys():
            return self.log_error("mandatory argument aliasName is missing")
        else:
            url += args.pop("aliasName")+"/"

        data = self._post( url, args)
        return data

    def list(self, args={}, params={}):
        """"""
        url = "firewall/alias_util/list/"
        data = {}

        if "aliasName" not in args.keys():
            return self.log_error("mandatory argument aliasName is missing")
        else:
            url += args.pop("aliasName")+"/"

        data = self._get( url, args)
        return data

    def update_bogons(self, args={}, params={}):
        """"""
        url = "firewall/alias_util/update_bogons/"
        data = {}

        data = self._get( url, args)
        return data

class firewall_category(client.BaseClient):
    """A client for interacting with the OPNSense's firewallcategory API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Category.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addItem(self, args={}, params={}):
        """"""
        url = "firewall/category/addItem/"
        data = {}

        data = self._post( url, args)
        return data

    def delItem(self, args={}, params={}):
        """"""
        url = "firewall/category/delItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "firewall/category/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getItem(self, args={}, params={}):
        """"""
        url = "firewall/category/getItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchItem(self, args={}, params={}):
        """"""
        url = "firewall/category/searchItem/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "firewall/category/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setItem(self, args={}, params={}):
        """"""
        url = "firewall/category/setItem/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
