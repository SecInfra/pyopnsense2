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

class nrpe_command(client.BaseClient):
    """A client for interacting with the OPNSense's nrpecommand API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net-mgmt/nrpe/src/opnsense/mvc/app/models/OPNsense/Nrpe/Command.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addCommand(self, args={}, params={}):
        """"""
        url = "nrpe/command/addCommand/"
        data = {}

        data = self._post( url, args)
        return data

    def delCommand(self, args={}, params={}):
        """"""
        url = "nrpe/command/delCommand/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "nrpe/command/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getCommand(self, args={}, params={}):
        """"""
        url = "nrpe/command/getCommand/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchCommand(self, args={}, params={}):
        """"""
        url = "nrpe/command/searchCommand/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "nrpe/command/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setCommand(self, args={}, params={}):
        """"""
        url = "nrpe/command/setCommand/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleCommand(self, args={}, params={}):
        """"""
        url = "nrpe/command/toggleCommand/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class nrpe_general(client.BaseClient):
    """A client for interacting with the OPNSense's nrpegeneral API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net-mgmt/nrpe/src/opnsense/mvc/app/models/OPNsense/Nrpe/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "nrpe/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "nrpe/general/set/"
        data = {}

        data = self._get( url, args)
        return data

class nrpe_service(client.BaseClient):
    """A client for interacting with the OPNSense's nrpeservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net-mgmt/nrpe/src/opnsense/mvc/app/models/OPNsense/Nrpe/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "nrpe/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "nrpe/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "nrpe/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "nrpe/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "nrpe/service/stop/"
        data = {}

        data = self._get( url, args)
        return data
