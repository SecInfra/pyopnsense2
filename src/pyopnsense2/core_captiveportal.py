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

class captiveportal_access(client.BaseClient):
    """A client for interacting with the OPNSense's captiveportalaccess API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def logoff(self, args={}, params={}):
        """"""
        url = "captiveportal/access/logoff/"
        data = {}

        if "zoneid" not in args.keys():
            return self.log_error("mandatory argument zoneid is missing")
        else:
            url += args.pop("zoneid")+"/"

        data = self._get( url, args)
        return data

    def logon(self, args={}, params={}):
        """"""
        url = "captiveportal/access/logon/"
        data = {}

        if "zoneid" not in args.keys():
            return self.log_error("mandatory argument zoneid is missing")
        else:
            url += args.pop("zoneid")+"/"

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "captiveportal/access/status/"
        data = {}

        if "zoneid" not in args.keys():
            return self.log_error("mandatory argument zoneid is missing")
        else:
            url += args.pop("zoneid")+"/"

        data = self._post( url, args)
        return data

class captiveportal_service(client.BaseClient):
    """A client for interacting with the OPNSense's captiveportalservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def delTemplate(self, args={}, params={}):
        """"""
        url = "captiveportal/service/delTemplate/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def getTemplate(self, args={}, params={}):
        """"""
        url = "captiveportal/service/getTemplate/"
        data = {}

        if "fileid" not in args.keys():
            return self.log_error("mandatory argument fileid is missing")
        else:
            url += args.pop("fileid")+"/"

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "captiveportal/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def saveTemplate(self, args={}, params={}):
        """"""
        url = "captiveportal/service/saveTemplate/"
        data = {}

        data = self._post( url, args)
        return data

    def searchTemplates(self, args={}, params={}):
        """"""
        url = "captiveportal/service/searchTemplates/"
        data = {}

        data = self._get( url, args)
        return data

class captiveportal_session(client.BaseClient):
    """A client for interacting with the OPNSense's captiveportalsession API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def connect(self, args={}, params={}):
        """"""
        url = "captiveportal/session/connect/"
        data = {}

        if "zoneid" not in args.keys():
            return self.log_error("mandatory argument zoneid is missing")
        else:
            url += args.pop("zoneid")+"/"

        data = self._post( url, args)
        return data

    def disconnect(self, args={}, params={}):
        """"""
        url = "captiveportal/session/disconnect/"
        data = {}

        if "zoneid" not in args.keys():
            return self.log_error("mandatory argument zoneid is missing")
        else:
            url += args.pop("zoneid")+"/"

        data = self._post( url, args)
        return data

    def list(self, args={}, params={}):
        """"""
        url = "captiveportal/session/list/"
        data = {}

        if "zoneid" not in args.keys():
            return self.log_error("mandatory argument zoneid is missing")
        else:
            url += args.pop("zoneid")+"/"

        data = self._get( url, args)
        return data

    def zones(self, args={}, params={}):
        """"""
        url = "captiveportal/session/zones/"
        data = {}

        data = self._get( url, args)
        return data

class captiveportal_settings(client.BaseClient):
    """A client for interacting with the OPNSense's captiveportalsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/CaptivePortal/CaptivePortal.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addZone(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/addZone/"
        data = {}

        data = self._post( url, args)
        return data

    def delZone(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/delZone/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getZone(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/getZone/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchZones(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/searchZones/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setZone(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/setZone/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleZone(self, args={}, params={}):
        """"""
        url = "captiveportal/settings/toggleZone/"
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

class captiveportal_voucher(client.BaseClient):
    """A client for interacting with the OPNSense's captiveportalvoucher API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def dropExpiredVouchers(self, args={}, params={}):
        """"""
        url = "captiveportal/voucher/dropExpiredVouchers/"
        data = {}

        if "group" not in args.keys():
            return self.log_error("mandatory argument group is missing")
        else:
            url += args.pop("group")+"/"

        if "provider" not in args.keys():
            return self.log_error("mandatory argument provider is missing")
        else:
            url += args.pop("provider")+"/"

        data = self._post( url, args)
        return data

    def dropVoucherGroup(self, args={}, params={}):
        """"""
        url = "captiveportal/voucher/dropVoucherGroup/"
        data = {}

        if "group" not in args.keys():
            return self.log_error("mandatory argument group is missing")
        else:
            url += args.pop("group")+"/"

        if "provider" not in args.keys():
            return self.log_error("mandatory argument provider is missing")
        else:
            url += args.pop("provider")+"/"

        data = self._post( url, args)
        return data

    def expireVoucher(self, args={}, params={}):
        """"""
        url = "captiveportal/voucher/expireVoucher/"
        data = {}

        if "provider" not in args.keys():
            return self.log_error("mandatory argument provider is missing")
        else:
            url += args.pop("provider")+"/"

        data = self._post( url, args)
        return data

    def generateVouchers(self, args={}, params={}):
        """"""
        url = "captiveportal/voucher/generateVouchers/"
        data = {}

        if "provider" not in args.keys():
            return self.log_error("mandatory argument provider is missing")
        else:
            url += args.pop("provider")+"/"

        data = self._post( url, args)
        return data

    def listProviders(self, args={}, params={}):
        """"""
        url = "captiveportal/voucher/listProviders/"
        data = {}

        data = self._get( url, args)
        return data

    def listVoucherGroups(self, args={}, params={}):
        """"""
        url = "captiveportal/voucher/listVoucherGroups/"
        data = {}

        if "provider" not in args.keys():
            return self.log_error("mandatory argument provider is missing")
        else:
            url += args.pop("provider")+"/"

        data = self._get( url, args)
        return data

    def listVouchers(self, args={}, params={}):
        """"""
        url = "captiveportal/voucher/listVouchers/"
        data = {}

        if "group" not in args.keys():
            return self.log_error("mandatory argument group is missing")
        else:
            url += args.pop("group")+"/"

        if "provider" not in args.keys():
            return self.log_error("mandatory argument provider is missing")
        else:
            url += args.pop("provider")+"/"

        data = self._get( url, args)
        return data
