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

class bind_acl(client.BaseClient):
    """A client for interacting with the OPNSense's bindacl API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Acl.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addAcl(self, args={}, params={}):
        """"""
        url = "bind/acl/addAcl/"
        data = {}

        data = self._post( url, args)
        return data

    def delAcl(self, args={}, params={}):
        """"""
        url = "bind/acl/delAcl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "bind/acl/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAcl(self, args={}, params={}):
        """"""
        url = "bind/acl/getAcl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchAcl(self, args={}, params={}):
        """"""
        url = "bind/acl/searchAcl/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "bind/acl/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setAcl(self, args={}, params={}):
        """"""
        url = "bind/acl/setAcl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleAcl(self, args={}, params={}):
        """"""
        url = "bind/acl/toggleAcl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class bind_dnsbl(client.BaseClient):
    """A client for interacting with the OPNSense's binddnsbl API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Dnsbl.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "bind/dnsbl/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "bind/dnsbl/set/"
        data = {}

        data = self._get( url, args)
        return data

class bind_domain(client.BaseClient):
    """A client for interacting with the OPNSense's binddomain API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Domain.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addDomain(self, args={}, params={}):
        """"""
        url = "bind/domain/addDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delDomain(self, args={}, params={}):
        """"""
        url = "bind/domain/delDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "bind/domain/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getDomain(self, args={}, params={}):
        """"""
        url = "bind/domain/getDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchDomain(self, args={}, params={}):
        """"""
        url = "bind/domain/searchDomain/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "bind/domain/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setDomain(self, args={}, params={}):
        """"""
        url = "bind/domain/setDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleDomain(self, args={}, params={}):
        """"""
        url = "bind/domain/toggleDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class bind_general(client.BaseClient):
    """A client for interacting with the OPNSense's bindgeneral API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "bind/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "bind/general/set/"
        data = {}

        data = self._get( url, args)
        return data

class bind_record(client.BaseClient):
    """A client for interacting with the OPNSense's bindrecord API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Record.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addRecord(self, args={}, params={}):
        """"""
        url = "bind/record/addRecord/"
        data = {}

        data = self._post( url, args)
        return data

    def delRecord(self, args={}, params={}):
        """"""
        url = "bind/record/delRecord/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "bind/record/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getRecord(self, args={}, params={}):
        """"""
        url = "bind/record/getRecord/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchRecord(self, args={}, params={}):
        """"""
        url = "bind/record/searchRecord/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "bind/record/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setRecord(self, args={}, params={}):
        """"""
        url = "bind/record/setRecord/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRecord(self, args={}, params={}):
        """"""
        url = "bind/record/toggleRecord/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class bind_service(client.BaseClient):
    """A client for interacting with the OPNSense's bindservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def dnsbl(self, args={}, params={}):
        """"""
        url = "bind/service/dnsbl/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "bind/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "bind/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "bind/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "bind/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "bind/service/stop/"
        data = {}

        data = self._get( url, args)
        return data
