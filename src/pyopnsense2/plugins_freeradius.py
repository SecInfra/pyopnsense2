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

class freeradius_avpair(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiusavpair API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Avpair.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addAvpair(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/addAvpair/"
        data = {}

        data = self._post( url, args)
        return data

    def delAvpair(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/delAvpair/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAvpair(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/getAvpair/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchAvpair(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/searchAvpair/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setAvpair(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/setAvpair/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleAvpair(self, args={}, params={}):
        """"""
        url = "freeradius/avpair/toggleAvpair/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class freeradius_client(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiusclient API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Client.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addClient(self, args={}, params={}):
        """"""
        url = "freeradius/client/addClient/"
        data = {}

        data = self._post( url, args)
        return data

    def delClient(self, args={}, params={}):
        """"""
        url = "freeradius/client/delClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/client/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getClient(self, args={}, params={}):
        """"""
        url = "freeradius/client/getClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchClient(self, args={}, params={}):
        """"""
        url = "freeradius/client/searchClient/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/client/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setClient(self, args={}, params={}):
        """"""
        url = "freeradius/client/setClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleClient(self, args={}, params={}):
        """"""
        url = "freeradius/client/toggleClient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

class freeradius_dhcp(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiusdhcp API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Dhcp.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addDhcp(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/addDhcp/"
        data = {}

        data = self._post( url, args)
        return data

    def delDhcp(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/delDhcp/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getDhcp(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/getDhcp/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchDhcp(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/searchDhcp/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setDhcp(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/setDhcp/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleDhcp(self, args={}, params={}):
        """"""
        url = "freeradius/dhcp/toggleDhcp/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class freeradius_eap(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiuseap API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/eap/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/eap/set/"
        data = {}

        data = self._post( url, args)
        return data

class freeradius_general(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiusgeneral API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/general/set/"
        data = {}

        data = self._post( url, args)
        return data

class freeradius_ldap(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiusldap API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Ldap.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/ldap/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/ldap/set/"
        data = {}

        data = self._get( url, args)
        return data

class freeradius_lease(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiuslease API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Lease.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addLease(self, args={}, params={}):
        """"""
        url = "freeradius/lease/addLease/"
        data = {}

        data = self._post( url, args)
        return data

    def delLease(self, args={}, params={}):
        """"""
        url = "freeradius/lease/delLease/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/lease/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getLease(self, args={}, params={}):
        """"""
        url = "freeradius/lease/getLease/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchLease(self, args={}, params={}):
        """"""
        url = "freeradius/lease/searchLease/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/lease/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setLease(self, args={}, params={}):
        """"""
        url = "freeradius/lease/setLease/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleLease(self, args={}, params={}):
        """"""
        url = "freeradius/lease/toggleLease/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class freeradius_service(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiusservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "freeradius/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "freeradius/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "freeradius/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "freeradius/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "freeradius/service/stop/"
        data = {}

        data = self._post( url, args)
        return data

class freeradius_user(client.BaseClient):
    """A client for interacting with the OPNSense's freeradiususer API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/User.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addUser(self, args={}, params={}):
        """"""
        url = "freeradius/user/addUser/"
        data = {}

        data = self._post( url, args)
        return data

    def delUser(self, args={}, params={}):
        """"""
        url = "freeradius/user/delUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "freeradius/user/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getUser(self, args={}, params={}):
        """"""
        url = "freeradius/user/getUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchUser(self, args={}, params={}):
        """"""
        url = "freeradius/user/searchUser/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "freeradius/user/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setUser(self, args={}, params={}):
        """"""
        url = "freeradius/user/setUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleUser(self, args={}, params={}):
        """"""
        url = "freeradius/user/toggleUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data
