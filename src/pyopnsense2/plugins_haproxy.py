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

class haproxy_export(client.BaseClient):
    """A client for interacting with the OPNSense's haproxyexport API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def config(self, args={}, params={}):
        """"""
        url = "haproxy/export/config/"
        data = {}

        data = self._get( url, args)
        return data

    def diff(self, args={}, params={}):
        """"""
        url = "haproxy/export/diff/"
        data = {}

        data = self._get( url, args)
        return data

    def download(self, args={}, params={}):
        """"""
        url = "haproxy/export/download/"
        data = {}

        if "type" not in args.keys():
            return self.log_error("mandatory argument type is missing")
        else:
            url += args.pop("type")+"/"

        data = self._get( url, args)
        return data

class haproxy_maintenance(client.BaseClient):
    """A client for interacting with the OPNSense's haproxymaintenance API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/haproxy/src/opnsense/mvc/app/models/OPNsense/HAProxy/HAProxy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def certActions(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/certActions/"
        data = {}

        data = self._get( url, args)
        return data

    def certDiff(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/certDiff/"
        data = {}

        data = self._get( url, args)
        return data

    def certSync(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/certSync/"
        data = {}

        data = self._get( url, args)
        return data

    def certSyncBulk(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/certSyncBulk/"
        data = {}

        data = self._get( url, args)
        return data

    def fetchCronIntegration(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/fetchCronIntegration/"
        data = {}

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/get/"
        data = {}

        data = self._get( url, args)
        return data

    def searchCertificateDiff(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/searchCertificateDiff/"
        data = {}

        data = self._get( url, args)
        return data

    def searchServer(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/searchServer/"
        data = {}

        data = self._get( url, args)
        return data

    def serverState(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/serverState/"
        data = {}

        data = self._get( url, args)
        return data

    def serverStateBulk(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/serverStateBulk/"
        data = {}

        data = self._get( url, args)
        return data

    def serverWeight(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/serverWeight/"
        data = {}

        data = self._get( url, args)
        return data

    def serverWeightBulk(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/serverWeightBulk/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "haproxy/maintenance/set/"
        data = {}

        data = self._get( url, args)
        return data

class haproxy_service(client.BaseClient):
    """A client for interacting with the OPNSense's haproxyservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/haproxy/src/opnsense/mvc/app/models/OPNsense/HAProxy/HAProxy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def configtest(self, args={}, params={}):
        """"""
        url = "haproxy/service/configtest/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "haproxy/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "haproxy/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "haproxy/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "haproxy/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "haproxy/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

class haproxy_settings(client.BaseClient):
    """A client for interacting with the OPNSense's haproxysettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/haproxy/src/opnsense/mvc/app/models/OPNsense/HAProxy/HAProxy.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addAcl(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addAcl/"
        data = {}

        data = self._post( url, args)
        return data

    def addAction(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addAction/"
        data = {}

        data = self._post( url, args)
        return data

    def addBackend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addBackend/"
        data = {}

        data = self._post( url, args)
        return data

    def addCpu(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addCpu/"
        data = {}

        data = self._post( url, args)
        return data

    def addErrorfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addErrorfile/"
        data = {}

        data = self._post( url, args)
        return data

    def addFrontend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addFrontend/"
        data = {}

        data = self._post( url, args)
        return data

    def addGroup(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addGroup/"
        data = {}

        data = self._post( url, args)
        return data

    def addHealthcheck(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addHealthcheck/"
        data = {}

        data = self._post( url, args)
        return data

    def addLua(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addLua/"
        data = {}

        data = self._post( url, args)
        return data

    def addMapfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addMapfile/"
        data = {}

        data = self._post( url, args)
        return data

    def addServer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addServer/"
        data = {}

        data = self._post( url, args)
        return data

    def addUser(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addUser/"
        data = {}

        data = self._post( url, args)
        return data

    def addmailer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addmailer/"
        data = {}

        data = self._post( url, args)
        return data

    def addresolver(self, args={}, params={}):
        """"""
        url = "haproxy/settings/addresolver/"
        data = {}

        data = self._post( url, args)
        return data

    def delAcl(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delAcl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delAction(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delAction/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delBackend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delBackend/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delCpu(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delCpu/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delErrorfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delErrorfile/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delFrontend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delFrontend/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delGroup(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delGroup/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delHealthcheck(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delHealthcheck/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delLua(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delLua/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delMapfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delMapfile/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delServer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delUser(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delmailer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delmailer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delresolver(self, args={}, params={}):
        """"""
        url = "haproxy/settings/delresolver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "haproxy/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAcl(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getAcl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getAction(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getAction/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getBackend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getBackend/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getCpu(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getCpu/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getErrorfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getErrorfile/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getFrontend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getFrontend/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getGroup(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getGroup/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getHealthcheck(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getHealthcheck/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getLua(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getLua/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getMapfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getMapfile/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getServer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getUser(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getmailer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getmailer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getresolver(self, args={}, params={}):
        """"""
        url = "haproxy/settings/getresolver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchAcls(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchAcls/"
        data = {}

        data = self._get( url, args)
        return data

    def searchActions(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchActions/"
        data = {}

        data = self._get( url, args)
        return data

    def searchBackends(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchBackends/"
        data = {}

        data = self._get( url, args)
        return data

    def searchCpus(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchCpus/"
        data = {}

        data = self._get( url, args)
        return data

    def searchErrorfiles(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchErrorfiles/"
        data = {}

        data = self._get( url, args)
        return data

    def searchFrontends(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchFrontends/"
        data = {}

        data = self._get( url, args)
        return data

    def searchGroups(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchGroups/"
        data = {}

        data = self._get( url, args)
        return data

    def searchHealthchecks(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchHealthchecks/"
        data = {}

        data = self._get( url, args)
        return data

    def searchLuas(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchLuas/"
        data = {}

        data = self._get( url, args)
        return data

    def searchMapfiles(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchMapfiles/"
        data = {}

        data = self._get( url, args)
        return data

    def searchServers(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchServers/"
        data = {}

        data = self._get( url, args)
        return data

    def searchUsers(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchUsers/"
        data = {}

        data = self._get( url, args)
        return data

    def searchmailers(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchmailers/"
        data = {}

        data = self._get( url, args)
        return data

    def searchresolvers(self, args={}, params={}):
        """"""
        url = "haproxy/settings/searchresolvers/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "haproxy/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setAcl(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setAcl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setAction(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setAction/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setBackend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setBackend/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setCpu(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setCpu/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setErrorfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setErrorfile/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setFrontend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setFrontend/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setGroup(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setGroup/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setHealthcheck(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setHealthcheck/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setLua(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setLua/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setMapfile(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setMapfile/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setServer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setServer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setUser(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setUser/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setmailer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setmailer/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setresolver(self, args={}, params={}):
        """"""
        url = "haproxy/settings/setresolver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleBackend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleBackend/"
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

    def toggleCpu(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleCpu/"
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

    def toggleFrontend(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleFrontend/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleGroup(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleGroup/"
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

    def toggleLua(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleLua/"
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

    def toggleServer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleServer/"
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

    def toggleUser(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleUser/"
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

    def togglemailer(self, args={}, params={}):
        """"""
        url = "haproxy/settings/togglemailer/"
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

    def toggleresolver(self, args={}, params={}):
        """"""
        url = "haproxy/settings/toggleresolver/"
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

class haproxy_statistics(client.BaseClient):
    """A client for interacting with the OPNSense's haproxystatistics API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def counters(self, args={}, params={}):
        """"""
        url = "haproxy/statistics/counters/"
        data = {}

        data = self._get( url, args)
        return data

    def info(self, args={}, params={}):
        """"""
        url = "haproxy/statistics/info/"
        data = {}

        data = self._get( url, args)
        return data

    def tables(self, args={}, params={}):
        """"""
        url = "haproxy/statistics/tables/"
        data = {}

        data = self._get( url, args)
        return data
