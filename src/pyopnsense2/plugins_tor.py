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

class tor_exitacl(client.BaseClient):
    """A client for interacting with the OPNSense's torexitacl API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/ACLExitPolicy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addacl(self, args={}, params={}):
        """"""
        url = "tor/exitacl/addacl/"
        data = {}

        data = self._post( url, args)
        return data

    def delacl(self, args={}, params={}):
        """"""
        url = "tor/exitacl/delacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "tor/exitacl/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getacl(self, args={}, params={}):
        """"""
        url = "tor/exitacl/getacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchacl(self, args={}, params={}):
        """"""
        url = "tor/exitacl/searchacl/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "tor/exitacl/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setacl(self, args={}, params={}):
        """"""
        url = "tor/exitacl/setacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleacl(self, args={}, params={}):
        """"""
        url = "tor/exitacl/toggleacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class tor_general(client.BaseClient):
    """A client for interacting with the OPNSense's torgeneral API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addhidservauth(self, args={}, params={}):
        """"""
        url = "tor/general/addhidservauth/"
        data = {}

        data = self._post( url, args)
        return data

    def delhidservauth(self, args={}, params={}):
        """"""
        url = "tor/general/delhidservauth/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "tor/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def gethidservauth(self, args={}, params={}):
        """"""
        url = "tor/general/gethidservauth/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchhidservauth(self, args={}, params={}):
        """"""
        url = "tor/general/searchhidservauth/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "tor/general/set/"
        data = {}

        data = self._get( url, args)
        return data

    def sethidservauth(self, args={}, params={}):
        """"""
        url = "tor/general/sethidservauth/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def togglehidservauth(self, args={}, params={}):
        """"""
        url = "tor/general/togglehidservauth/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class tor_hiddenservice(client.BaseClient):
    """A client for interacting with the OPNSense's torhiddenservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/HiddenService.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addservice(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/addservice/"
        data = {}

        data = self._post( url, args)
        return data

    def delservice(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/delservice/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getservice(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/getservice/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchservice(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/searchservice/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setservice(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/setservice/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleservice(self, args={}, params={}):
        """"""
        url = "tor/hiddenservice/toggleservice/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class tor_hiddenserviceacl(client.BaseClient):
    """A client for interacting with the OPNSense's torhiddenserviceacl API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/HiddenServiceACL.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addacl(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/addacl/"
        data = {}

        data = self._post( url, args)
        return data

    def delacl(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/delacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getacl(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/getacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchacl(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/searchacl/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setacl(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/setacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleacl(self, args={}, params={}):
        """"""
        url = "tor/hiddenserviceacl/toggleacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class tor_relay(client.BaseClient):
    """A client for interacting with the OPNSense's torrelay API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/Relay.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "tor/relay/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "tor/relay/set/"
        data = {}

        data = self._get( url, args)
        return data

class tor_service(client.BaseClient):
    """A client for interacting with the OPNSense's torservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def circuits(self, args={}, params={}):
        """"""
        url = "tor/service/circuits/"
        data = {}

        data = self._get( url, args)
        return data

    def get_hidden_services(self, args={}, params={}):
        """"""
        url = "tor/service/get_hidden_services/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "tor/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "tor/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "tor/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "tor/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "tor/service/stop/"
        data = {}

        data = self._post( url, args)
        return data

    def streams(self, args={}, params={}):
        """"""
        url = "tor/service/streams/"
        data = {}

        data = self._get( url, args)
        return data

class tor_socksacl(client.BaseClient):
    """A client for interacting with the OPNSense's torsocksacl API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/ACLSocksPolicy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addacl(self, args={}, params={}):
        """"""
        url = "tor/socksacl/addacl/"
        data = {}

        data = self._post( url, args)
        return data

    def delacl(self, args={}, params={}):
        """"""
        url = "tor/socksacl/delacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "tor/socksacl/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getacl(self, args={}, params={}):
        """"""
        url = "tor/socksacl/getacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchacl(self, args={}, params={}):
        """"""
        url = "tor/socksacl/searchacl/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "tor/socksacl/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setacl(self, args={}, params={}):
        """"""
        url = "tor/socksacl/setacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleacl(self, args={}, params={}):
        """"""
        url = "tor/socksacl/toggleacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
