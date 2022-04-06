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

class siproxd_domain(client.BaseClient):
    """A client for interacting with the OPNSense's siproxddomain API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/siproxd/src/opnsense/mvc/app/models/OPNsense/Siproxd/Domain.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addDomain(self, args={}, params={}):
        """"""
        url = "siproxd/domain/addDomain/"
        data = {}

        data = self._post( url, args)
        return data

    def delDomain(self, args={}, params={}):
        """"""
        url = "siproxd/domain/delDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "siproxd/domain/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getDomain(self, args={}, params={}):
        """"""
        url = "siproxd/domain/getDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchDomain(self, args={}, params={}):
        """"""
        url = "siproxd/domain/searchDomain/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "siproxd/domain/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setDomain(self, args={}, params={}):
        """"""
        url = "siproxd/domain/setDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleDomain(self, args={}, params={}):
        """"""
        url = "siproxd/domain/toggleDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

class siproxd_general(client.BaseClient):
    """A client for interacting with the OPNSense's siproxdgeneral API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "siproxd/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "siproxd/general/set/"
        data = {}

        data = self._post( url, args)
        return data

class siproxd_service(client.BaseClient):
    """A client for interacting with the OPNSense's siproxdservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "siproxd/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "siproxd/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def showregistrations(self, args={}, params={}):
        """"""
        url = "siproxd/service/showregistrations/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "siproxd/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "siproxd/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "siproxd/service/stop/"
        data = {}

        data = self._post( url, args)
        return data

class siproxd_user(client.BaseClient):
    """A client for interacting with the OPNSense's siproxduser API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/siproxd/src/opnsense/mvc/app/models/OPNsense/Siproxd/User.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addUser(self, args={}, params={}):
        """"""
        url = "siproxd/user/addUser/"
        data = {}

        data = self._post( url, args)
        return data

    def delUser(self, args={}, params={}):
        """"""
        url = "siproxd/user/delUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "siproxd/user/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getUser(self, args={}, params={}):
        """"""
        url = "siproxd/user/getUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchUser(self, args={}, params={}):
        """"""
        url = "siproxd/user/searchUser/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "siproxd/user/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setUser(self, args={}, params={}):
        """"""
        url = "siproxd/user/setUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleUser(self, args={}, params={}):
        """"""
        url = "siproxd/user/toggleUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data
