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

class quagga_bgp(client.BaseClient):
    """A client for interacting with the OPNSense's quaggabgp API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/BGP.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addAspath(self, args={}, params={}):
        """"""
        url = "quagga/bgp/addAspath/"
        data = {}

        data = self._post( url, args)
        return data

    def addCommunitylist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/addCommunitylist/"
        data = {}

        data = self._post( url, args)
        return data

    def addNeighbor(self, args={}, params={}):
        """"""
        url = "quagga/bgp/addNeighbor/"
        data = {}

        data = self._post( url, args)
        return data

    def addPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/addPrefixlist/"
        data = {}

        data = self._post( url, args)
        return data

    def addRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/bgp/addRoutemap/"
        data = {}

        data = self._post( url, args)
        return data

    def delAspath(self, args={}, params={}):
        """"""
        url = "quagga/bgp/delAspath/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delCommunitylist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/delCommunitylist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delNeighbor(self, args={}, params={}):
        """"""
        url = "quagga/bgp/delNeighbor/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/delPrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/bgp/delRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "quagga/bgp/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAspath(self, args={}, params={}):
        """"""
        url = "quagga/bgp/getAspath/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getCommunitylist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/getCommunitylist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getNeighbor(self, args={}, params={}):
        """"""
        url = "quagga/bgp/getNeighbor/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/getPrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/bgp/getRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchAspath(self, args={}, params={}):
        """"""
        url = "quagga/bgp/searchAspath/"
        data = {}

        data = self._get( url, args)
        return data

    def searchCommunitylist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/searchCommunitylist/"
        data = {}

        data = self._get( url, args)
        return data

    def searchNeighbor(self, args={}, params={}):
        """"""
        url = "quagga/bgp/searchNeighbor/"
        data = {}

        data = self._get( url, args)
        return data

    def searchPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/searchPrefixlist/"
        data = {}

        data = self._get( url, args)
        return data

    def searchRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/bgp/searchRoutemap/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "quagga/bgp/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setAspath(self, args={}, params={}):
        """"""
        url = "quagga/bgp/setAspath/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setCommunitylist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/setCommunitylist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setNeighbor(self, args={}, params={}):
        """"""
        url = "quagga/bgp/setNeighbor/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/setPrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/bgp/setRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleAspath(self, args={}, params={}):
        """"""
        url = "quagga/bgp/toggleAspath/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleNeighbor(self, args={}, params={}):
        """"""
        url = "quagga/bgp/toggleNeighbor/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def togglePrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/bgp/togglePrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/bgp/toggleRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class quagga_diagnostics(client.BaseClient):
    """A client for interacting with the OPNSense's quaggadiagnostics API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def bgpneighbors(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/bgpneighbors/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def bgproute(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/bgproute/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def bgproute4(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/bgproute4/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def bgproute6(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/bgproute6/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def bgpsummary(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/bgpsummary/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def generalroute(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/generalroute/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def generalroute4(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/generalroute4/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def generalroute6(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/generalroute6/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def generalrunningconfig(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/generalrunningconfig/"
        data = {}

        data = self._get( url, args)
        return data

    def ospfdatabase(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfdatabase/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfinterface(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfinterface/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfneighbor(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfneighbor/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfoverview(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfoverview/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfroute(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfroute/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfv3database(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfv3database/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfv3interface(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfv3interface/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfv3neighbor(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfv3neighbor/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfv3overview(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfv3overview/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

    def ospfv3route(self, args={}, params={}):
        """"""
        url = "quagga/diagnostics/ospfv3route/"
        data = {}

        if "format" not in args.keys():
            return self.log_error("mandatory argument format is missing")
        else:
            url += args.pop("format")+"/"

        data = self._get( url, args)
        return data

class quagga_general(client.BaseClient):
    """A client for interacting with the OPNSense's quaggageneral API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "quagga/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "quagga/general/set/"
        data = {}

        data = self._post( url, args)
        return data

class quagga_ospf6settings(client.BaseClient):
    """A client for interacting with the OPNSense's quaggaospf6settings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/OSPF6.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/addInterface/"
        data = {}

        data = self._post( url, args)
        return data

    def delInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/delInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/getInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/searchInterface/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/setInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospf6settings/toggleInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class quagga_ospfsettings(client.BaseClient):
    """A client for interacting with the OPNSense's quaggaospfsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/OSPF.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/addInterface/"
        data = {}

        data = self._post( url, args)
        return data

    def addNetwork(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/addNetwork/"
        data = {}

        data = self._post( url, args)
        return data

    def addPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/addPrefixlist/"
        data = {}

        data = self._post( url, args)
        return data

    def addRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/addRoutemap/"
        data = {}

        data = self._post( url, args)
        return data

    def delInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/delInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delNetwork(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/delNetwork/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/delPrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/delRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/getInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getNetwork(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/getNetwork/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/getPrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/getRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/searchInterface/"
        data = {}

        data = self._get( url, args)
        return data

    def searchNetwork(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/searchNetwork/"
        data = {}

        data = self._get( url, args)
        return data

    def searchPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/searchPrefixlist/"
        data = {}

        data = self._get( url, args)
        return data

    def searchRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/searchRoutemap/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/setInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setNetwork(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/setNetwork/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setPrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/setPrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/setRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleInterface(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/toggleInterface/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleNetwork(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/toggleNetwork/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def togglePrefixlist(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/togglePrefixlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRoutemap(self, args={}, params={}):
        """"""
        url = "quagga/ospfsettings/toggleRoutemap/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class quagga_rip(client.BaseClient):
    """A client for interacting with the OPNSense's quaggarip API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/RIP.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "quagga/rip/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "quagga/rip/set/"
        data = {}

        data = self._get( url, args)
        return data

class quagga_service(client.BaseClient):
    """A client for interacting with the OPNSense's quaggaservice API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "quagga/service/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "quagga/service/restart/"
        data = {}

        data = self._post( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "quagga/service/start/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "quagga/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "quagga/service/stop/"
        data = {}

        data = self._post( url, args)
        return data
