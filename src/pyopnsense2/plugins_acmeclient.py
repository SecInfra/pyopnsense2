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

class acmeclient_accounts(client.BaseClient):
    """A client for interacting with the OPNSense's acmeclientaccounts API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def add(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/add/"
        data = {}

        data = self._post( url, args)
        return data

    def del(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/del/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/get/"
        data = {}

        data = self._get( url, args)
        return data

    def register(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/register/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def search(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/search/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/set/"
        data = {}

        data = self._get( url, args)
        return data

    def toggle(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/toggle/"
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

    def update(self, args={}, params={}):
        """"""
        url = "acmeclient/accounts/update/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class acmeclient_actions(client.BaseClient):
    """A client for interacting with the OPNSense's acmeclientactions API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def add(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/add/"
        data = {}

        data = self._post( url, args)
        return data

    def del(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/del/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/get/"
        data = {}

        data = self._get( url, args)
        return data

    def search(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/search/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/set/"
        data = {}

        data = self._get( url, args)
        return data

    def sftpGetIdentity(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/sftpGetIdentity/"
        data = {}

        data = self._get( url, args)
        return data

    def sftpTestConnection(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/sftpTestConnection/"
        data = {}

        data = self._get( url, args)
        return data

    def toggle(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/toggle/"
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

    def update(self, args={}, params={}):
        """"""
        url = "acmeclient/actions/update/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class acmeclient_certificates(client.BaseClient):
    """A client for interacting with the OPNSense's acmeclientcertificates API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def add(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/add/"
        data = {}

        data = self._post( url, args)
        return data

    def automation(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/automation/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def del(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/del/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/get/"
        data = {}

        data = self._get( url, args)
        return data

    def removekey(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/removekey/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def revoke(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/revoke/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def search(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/search/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/set/"
        data = {}

        data = self._get( url, args)
        return data

    def sign(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/sign/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggle(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/toggle/"
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

    def update(self, args={}, params={}):
        """"""
        url = "acmeclient/certificates/update/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class acmeclient_service(client.BaseClient):
    """A client for interacting with the OPNSense's acmeclientservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def configtest(self, args={}, params={}):
        """"""
        url = "acmeclient/service/configtest/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "acmeclient/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def reset(self, args={}, params={}):
        """"""
        url = "acmeclient/service/reset/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "acmeclient/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def signallcerts(self, args={}, params={}):
        """"""
        url = "acmeclient/service/signallcerts/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "acmeclient/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "acmeclient/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "acmeclient/service/stop/"
        data = {}

        data = self._post( url, args)
        return data

class acmeclient_settings(client.BaseClient):
    """A client for interacting with the OPNSense's acmeclientsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def fetchCronIntegration(self, args={}, params={}):
        """"""
        url = "acmeclient/settings/fetchCronIntegration/"
        data = {}

        data = self._post( url, args)
        return data

    def fetchHAProxyIntegration(self, args={}, params={}):
        """"""
        url = "acmeclient/settings/fetchHAProxyIntegration/"
        data = {}

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "acmeclient/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getBindPluginStatus(self, args={}, params={}):
        """"""
        url = "acmeclient/settings/getBindPluginStatus/"
        data = {}

        data = self._get( url, args)
        return data

    def getGcloudPluginStatus(self, args={}, params={}):
        """"""
        url = "acmeclient/settings/getGcloudPluginStatus/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "acmeclient/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

class acmeclient_validations(client.BaseClient):
    """A client for interacting with the OPNSense's acmeclientvalidations API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def add(self, args={}, params={}):
        """"""
        url = "acmeclient/validations/add/"
        data = {}

        data = self._post( url, args)
        return data

    def del(self, args={}, params={}):
        """"""
        url = "acmeclient/validations/del/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "acmeclient/validations/get/"
        data = {}

        data = self._get( url, args)
        return data

    def search(self, args={}, params={}):
        """"""
        url = "acmeclient/validations/search/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "acmeclient/validations/set/"
        data = {}

        data = self._get( url, args)
        return data

    def toggle(self, args={}, params={}):
        """"""
        url = "acmeclient/validations/toggle/"
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

    def update(self, args={}, params={}):
        """"""
        url = "acmeclient/validations/update/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
