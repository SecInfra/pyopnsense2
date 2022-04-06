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

class dnscryptproxy_cloak(client.BaseClient):
    """A client for interacting with the OPNSense's dnscryptproxycloak API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Cloak.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addCloak(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/addCloak/"
        data = {}

        data = self._post( url, args)
        return data

    def delCloak(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/delCloak/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getCloak(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/getCloak/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchCloak(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/searchCloak/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setCloak(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/setCloak/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleCloak(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/cloak/toggleCloak/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class dnscryptproxy_dnsbl(client.BaseClient):
    """A client for interacting with the OPNSense's dnscryptproxydnsbl API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Dnsbl.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/dnsbl/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/dnsbl/set/"
        data = {}

        data = self._get( url, args)
        return data

class dnscryptproxy_forward(client.BaseClient):
    """A client for interacting with the OPNSense's dnscryptproxyforward API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Forward.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addForward(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/addForward/"
        data = {}

        data = self._post( url, args)
        return data

    def delForward(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/delForward/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getForward(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/getForward/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchForward(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/searchForward/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setForward(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/setForward/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleForward(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/forward/toggleForward/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class dnscryptproxy_general(client.BaseClient):
    """A client for interacting with the OPNSense's dnscryptproxygeneral API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/general/set/"
        data = {}

        data = self._get( url, args)
        return data

class dnscryptproxy_server(client.BaseClient):
    """A client for interacting with the OPNSense's dnscryptproxyserver API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Server.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addServer(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/addServer/"
        data = {}

        data = self._post( url, args)
        return data

    def delServer(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/delServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getServer(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/getServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchServer(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/searchServer/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setServer(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/setServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleServer(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/server/toggleServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class dnscryptproxy_service(client.BaseClient):
    """A client for interacting with the OPNSense's dnscryptproxyservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def dnsbl(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/service/dnsbl/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

class dnscryptproxy_whitelist(client.BaseClient):
    """A client for interacting with the OPNSense's dnscryptproxywhitelist API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Whitelist.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addWhitelist(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/addWhitelist/"
        data = {}

        data = self._post( url, args)
        return data

    def delWhitelist(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/delWhitelist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getWhitelist(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/getWhitelist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchWhitelist(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/searchWhitelist/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setWhitelist(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/setWhitelist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleWhitelist(self, args={}, params={}):
        """"""
        url = "dnscryptproxy/whitelist/toggleWhitelist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
