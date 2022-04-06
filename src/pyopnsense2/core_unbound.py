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

class unbound_diagnostics(client.BaseClient):
    """A client for interacting with the OPNSense's unbounddiagnostics API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def dumpcache(self, args={}, params={}):
        """"""
        url = "unbound/diagnostics/dumpcache/"
        data = {}

        data = self._get( url, args)
        return data

    def dumpinfra(self, args={}, params={}):
        """"""
        url = "unbound/diagnostics/dumpinfra/"
        data = {}

        data = self._get( url, args)
        return data

    def listinsecure(self, args={}, params={}):
        """"""
        url = "unbound/diagnostics/listinsecure/"
        data = {}

        data = self._get( url, args)
        return data

    def listlocaldata(self, args={}, params={}):
        """"""
        url = "unbound/diagnostics/listlocaldata/"
        data = {}

        data = self._get( url, args)
        return data

    def listlocalzones(self, args={}, params={}):
        """"""
        url = "unbound/diagnostics/listlocalzones/"
        data = {}

        data = self._get( url, args)
        return data

    def stats(self, args={}, params={}):
        """"""
        url = "unbound/diagnostics/stats/"
        data = {}

        data = self._get( url, args)
        return data

class unbound_dnsbl(client.BaseClient):
    """A client for interacting with the OPNSense's unbounddnsbl API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unboundplus/Dnsbl.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "unbound/dnsbl/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "unbound/dnsbl/set/"
        data = {}

        data = self._get( url, args)
        return data

class unbound_miscellaneous(client.BaseClient):
    """A client for interacting with the OPNSense's unboundmiscellaneous API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unboundplus/Miscellaneous.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "unbound/miscellaneous/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "unbound/miscellaneous/set/"
        data = {}

        data = self._get( url, args)
        return data

class unbound_service(client.BaseClient):
    """A client for interacting with the OPNSense's unboundservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unboundplus/Dnsbl.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def dnsbl(self, args={}, params={}):
        """"""
        url = "unbound/service/dnsbl/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "unbound/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "unbound/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "unbound/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "unbound/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "unbound/service/stop/"
        data = {}

        data = self._get( url, args)
        return data
