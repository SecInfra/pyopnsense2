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

class firewall_filter(client.BaseClient):
    """A client for interacting with the OPNSense's firewallfilter API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addRule(self, args={}, params={}):
        """"""
        url = "firewall/filter/addRule/"
        data = {}

        data = self._post( url, args)
        return data

    def delRule(self, args={}, params={}):
        """"""
        url = "firewall/filter/delRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def getRule(self, args={}, params={}):
        """"""
        url = "firewall/filter/getRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchRule(self, args={}, params={}):
        """"""
        url = "firewall/filter/searchRule/"
        data = {}

        data = self._get( url, args)
        return data

    def setRule(self, args={}, params={}):
        """"""
        url = "firewall/filter/setRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRule(self, args={}, params={}):
        """"""
        url = "firewall/filter/toggleRule/"
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
    
    def savepoint(self, args={}, params={}):
        """"""
        url = "firewall/filter/savepoint/"
        data = {}

        data = self._post( url, args)
        return data
    
    def apply(self, args={}, params={}):
        """"""
        url = "firewall/filter/apply/"
        data = {}

        if "rollback_revision" in args.keys():
            url += args.pop("rollback_revision")+"/"

        data = self._post( url, args)
        return data
    
    def cancelRollback(self, args={}, params={}):
        """"""
        url = "firewall/filter/cancelRollback/"
        data = {}

        if "rollback_revision" not in args.keys():
            return self.log_error("mandatory argument rollback_revision is missing")
        else:
            url += args.pop("rollback_revision")+"/"

        data = self._post( url, args)
        return data
    
    def revert(self, args={}, params={}):
        """"""
        url = "firewall/filter/revert/"
        data = {}

        if "revision" not in args.keys():
            return self.log_error("mandatory argument revision is missing")
        else:
            url += args.pop("revision")+"/"

        data = self._post( url, args)
        return data

class firewall_filter_base(client.BaseClient):
    """A client for interacting with the OPNSense's firewallfilter_base API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/firewall/src/opnsense/mvc/app/models/OPNsense/Firewall/Filter.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def apply(self, args={}, params={}):
        """"""
        url = "firewall/filter_base/apply/"
        data = {}

        if "rollback_revision" not in args.keys():
            return self.log_error("mandatory argument rollback_revision is missing")
        else:
            url += args.pop("rollback_revision")+"/"

        data = self._post( url, args)
        return data

    def cancelRollback(self, args={}, params={}):
        """"""
        url = "firewall/filter_base/cancelRollback/"
        data = {}

        if "rollback_revision" not in args.keys():
            return self.log_error("mandatory argument rollback_revision is missing")
        else:
            url += args.pop("rollback_revision")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "firewall/filter_base/get/"
        data = {}

        data = self._get( url, args)
        return data

    def revert(self, args={}, params={}):
        """"""
        url = "firewall/filter_base/revert/"
        data = {}

        if "revision" not in args.keys():
            return self.log_error("mandatory argument revision is missing")
        else:
            url += args.pop("revision")+"/"

        data = self._post( url, args)
        return data

    def savepoint(self, args={}, params={}):
        """"""
        url = "firewall/filter_base/savepoint/"
        data = {}

        data = self._post( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "firewall/filter_base/set/"
        data = {}

        data = self._get( url, args)
        return data

class firewall_source_nat(client.BaseClient):
    """A client for interacting with the OPNSense's firewallsource_nat API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addRule(self, args={}, params={}):
        """"""
        url = "firewall/source_nat/addRule/"
        data = {}

        data = self._post( url, args)
        return data

    def delRule(self, args={}, params={}):
        """"""
        url = "firewall/source_nat/delRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def getRule(self, args={}, params={}):
        """"""
        url = "firewall/source_nat/getRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchRule(self, args={}, params={}):
        """"""
        url = "firewall/source_nat/searchRule/"
        data = {}

        data = self._get( url, args)
        return data

    def setRule(self, args={}, params={}):
        """"""
        url = "firewall/source_nat/setRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRule(self, args={}, params={}):
        """"""
        url = "firewall/source_nat/toggleRule/"
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
