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

class ids_service(client.BaseClient):
    """A client for interacting with the OPNSense's idsservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IDS/IDS.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def dropAlertLog(self, args={}, params={}):
        """"""
        url = "ids/service/dropAlertLog/"
        data = {}

        data = self._post( url, args)
        return data

    def getAlertInfo(self, args={}, params={}):
        """"""
        url = "ids/service/getAlertInfo/"
        data = {}

        if "alertId" not in args.keys():
            return self.log_error("mandatory argument alertId is missing")
        else:
            url += args.pop("alertId")+"/"

        if "fileid" not in args.keys():
            return self.log_error("mandatory argument fileid is missing")
        else:
            url += args.pop("fileid")+"/"

        data = self._get( url, args)
        return data

    def getAlertLogs(self, args={}, params={}):
        """"""
        url = "ids/service/getAlertLogs/"
        data = {}

        data = self._get( url, args)
        return data

    def queryAlerts(self, args={}, params={}):
        """"""
        url = "ids/service/queryAlerts/"
        data = {}

        data = self._post( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "ids/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def reloadRules(self, args={}, params={}):
        """"""
        url = "ids/service/reloadRules/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "ids/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "ids/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "ids/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "ids/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

    def updateRules(self, args={}, params={}):
        """"""
        url = "ids/service/updateRules/"
        data = {}

        if "wait" not in args.keys():
            return self.log_error("mandatory argument wait is missing")
        else:
            url += args.pop("wait")+"/"

        data = self._post( url, args)
        return data

class ids_settings(client.BaseClient):
    """A client for interacting with the OPNSense's idssettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IDS/IDS.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addPolicy(self, args={}, params={}):
        """"""
        url = "ids/settings/addPolicy/"
        data = {}

        data = self._post( url, args)
        return data

    def addPolicyRule(self, args={}, params={}):
        """"""
        url = "ids/settings/addPolicyRule/"
        data = {}

        data = self._post( url, args)
        return data

    def addUserRule(self, args={}, params={}):
        """"""
        url = "ids/settings/addUserRule/"
        data = {}

        data = self._post( url, args)
        return data

    def checkPolicyRule(self, args={}, params={}):
        """"""
        url = "ids/settings/checkPolicyRule/"
        data = {}

        data = self._get( url, args)
        return data

    def delPolicy(self, args={}, params={}):
        """"""
        url = "ids/settings/delPolicy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delPolicyRule(self, args={}, params={}):
        """"""
        url = "ids/settings/delPolicyRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delUserRule(self, args={}, params={}):
        """"""
        url = "ids/settings/delUserRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "ids/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getPolicy(self, args={}, params={}):
        """"""
        url = "ids/settings/getPolicy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getPolicyRule(self, args={}, params={}):
        """"""
        url = "ids/settings/getPolicyRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getRuleInfo(self, args={}, params={}):
        """"""
        url = "ids/settings/getRuleInfo/"
        data = {}

        if "sid" not in args.keys():
            return self.log_error("mandatory argument sid is missing")
        else:
            url += args.pop("sid")+"/"

        data = self._get( url, args)
        return data

    def getRuleset(self, args={}, params={}):
        """"""
        url = "ids/settings/getRuleset/"
        data = {}

        if "id" not in args.keys():
            return self.log_error("mandatory argument id is missing")
        else:
            url += args.pop("id")+"/"

        data = self._get( url, args)
        return data

    def getRulesetproperties(self, args={}, params={}):
        """"""
        url = "ids/settings/getRulesetproperties/"
        data = {}

        data = self._get( url, args)
        return data

    def getUserRule(self, args={}, params={}):
        """"""
        url = "ids/settings/getUserRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def listRuleMetadata(self, args={}, params={}):
        """"""
        url = "ids/settings/listRuleMetadata/"
        data = {}

        data = self._get( url, args)
        return data

    def listRulesets(self, args={}, params={}):
        """"""
        url = "ids/settings/listRulesets/"
        data = {}

        data = self._get( url, args)
        return data

    def searchInstalledRules(self, args={}, params={}):
        """"""
        url = "ids/settings/searchInstalledRules/"
        data = {}

        data = self._post( url, args)
        return data

    def searchPolicy(self, args={}, params={}):
        """"""
        url = "ids/settings/searchPolicy/"
        data = {}

        data = self._get( url, args)
        return data

    def searchPolicyRule(self, args={}, params={}):
        """"""
        url = "ids/settings/searchPolicyRule/"
        data = {}

        data = self._get( url, args)
        return data

    def searchUserRule(self, args={}, params={}):
        """"""
        url = "ids/settings/searchUserRule/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "ids/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setPolicy(self, args={}, params={}):
        """"""
        url = "ids/settings/setPolicy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setPolicyRule(self, args={}, params={}):
        """"""
        url = "ids/settings/setPolicyRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setRule(self, args={}, params={}):
        """"""
        url = "ids/settings/setRule/"
        data = {}

        if "sid" not in args.keys():
            return self.log_error("mandatory argument sid is missing")
        else:
            url += args.pop("sid")+"/"

        data = self._post( url, args)
        return data

    def setRuleset(self, args={}, params={}):
        """"""
        url = "ids/settings/setRuleset/"
        data = {}

        if "filename" not in args.keys():
            return self.log_error("mandatory argument filename is missing")
        else:
            url += args.pop("filename")+"/"

        data = self._post( url, args)
        return data

    def setRulesetproperties(self, args={}, params={}):
        """"""
        url = "ids/settings/setRulesetproperties/"
        data = {}

        data = self._post( url, args)
        return data

    def setUserRule(self, args={}, params={}):
        """"""
        url = "ids/settings/setUserRule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def togglePolicy(self, args={}, params={}):
        """"""
        url = "ids/settings/togglePolicy/"
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

    def togglePolicyRule(self, args={}, params={}):
        """"""
        url = "ids/settings/togglePolicyRule/"
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

    def toggleRule(self, args={}, params={}):
        """"""
        url = "ids/settings/toggleRule/"
        data = {}

        if "enabled" not in args.keys():
            return self.log_error("mandatory argument enabled is missing")
        else:
            url += args.pop("enabled")+"/"

        if "sids" not in args.keys():
            return self.log_error("mandatory argument sids is missing")
        else:
            url += args.pop("sids")+"/"

        data = self._post( url, args)
        return data

    def toggleRuleset(self, args={}, params={}):
        """"""
        url = "ids/settings/toggleRuleset/"
        data = {}

        if "enabled" not in args.keys():
            return self.log_error("mandatory argument enabled is missing")
        else:
            url += args.pop("enabled")+"/"

        if "filenames" not in args.keys():
            return self.log_error("mandatory argument filenames is missing")
        else:
            url += args.pop("filenames")+"/"

        data = self._post( url, args)
        return data

    def toggleUserRule(self, args={}, params={}):
        """"""
        url = "ids/settings/toggleUserRule/"
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
