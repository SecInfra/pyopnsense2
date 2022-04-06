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

class diagnostics_activity(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticsactivity API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def getActivity(self, args={}, params={}):
        """"""
        url = "diagnostics/activity/getActivity/"
        data = {}

        data = self._get( url, args)
        return data

class diagnostics_dns(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticsdns API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reverse_lookup(self, args={}, params={}):
        """"""
        url = "diagnostics/dns/reverse_lookup/"
        data = {}

        data = self._get( url, args)
        return data

class diagnostics_firewall(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticsfirewall API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def log(self, args={}, params={}):
        """"""
        url = f"diagnostics/firewall/log/?limit={args.get('limit')}" 
        data = {}

        data = self._get( url, args)
        return data

    def log_filters(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/log_filters/"
        data = {}

        data = self._get( url, args)
        return data

    def stats(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/stats/"
        data = {}

        data = self._get( url, args)
        return data

    def pfStatistcs(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/pfStatistcs/"
        data = {}

        data = self._get( url, args)
        return data

    def killStates(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/killStates/"
        data = {}

        data = self._post( url, args)
        return data

    def flushStates(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/flushStates/"
        data = {}

        data = self._post( url, args)
        return data

    def flushSources(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/flushSources/"
        data = {}

        data = self._post( url, args)
        return data

    def delState(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/delState/"
        data = {}

        if "stateid" not in args.keys():
            return self.log_error("mandatory argument stateid is missing")
        else:
            url += args.pop("stateid")

        data = self._post( url, args)
        return data

    def queryStates(self, args={}, params={}):
        """"""
        url = "diagnostics/firewall/queryStates/"
        data = {}

        data = self._post( url, args)
        return data

class diagnostics_interface(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticsinterface API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def delRoute(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/delRoute/"
        data = {}

        data = self._post( url, args)
        return data

    def flushArp(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/flushArp/"
        data = {}

        data = self._post( url, args)
        return data

    def getArp(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getArp/"
        data = {}

        data = self._get( url, args)
        return data

    def getBpfStatistics(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getBpfStatistics/"
        data = {}

        data = self._get( url, args)
        return data

    def getInterfaceNames(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getInterfaceNames/"
        data = {}

        data = self._get( url, args)
        return data

    def getInterfaceStatistics(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getInterfaceStatistics/"
        data = {}

        data = self._get( url, args)
        return data

    def getMemoryStatistics(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getMemoryStatistics/"
        data = {}

        data = self._get( url, args)
        return data

    def getNdp(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getNdp/"
        data = {}

        data = self._get( url, args)
        return data

    def getNetisrStatistics(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getNetisrStatistics/"
        data = {}

        data = self._get( url, args)
        return data

    def getProtocolStatistics(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getProtocolStatistics/"
        data = {}

        data = self._get( url, args)
        return data

    def getRoutes(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getRoutes/"
        data = {}

        data = self._get( url, args)
        return data

    def getSocketStatistics(self, args={}, params={}):
        """"""
        url = "diagnostics/interface/getSocketStatistics/"
        data = {}

        data = self._get( url, args)
        return data

class diagnostics_netflow(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticsnetflow API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def cacheStats(self, args={}, params={}):
        """"""
        url = "diagnostics/netflow/cacheStats/"
        data = {}

        data = self._get( url, args)
        return data

    def getconfig(self, args={}, params={}):
        """"""
        url = "diagnostics/netflow/getconfig/"
        data = {}

        data = self._get( url, args)
        return data

    def isEnabled(self, args={}, params={}):
        """"""
        url = "diagnostics/netflow/isEnabled/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "diagnostics/netflow/reconfigure/"
        data = {}

        data = self._post( url, args)
        return data

    def setconfig(self, args={}, params={}):
        """"""
        url = "diagnostics/netflow/setconfig/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "diagnostics/netflow/status/"
        data = {}

        data = self._get( url, args)
        return data

class diagnostics_networkinsight(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticsnetworkinsight API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def getInterfaces(self, args={}, params={}):
        """"""
        url = "diagnostics/networkinsight/getInterfaces/"
        data = {}

        data = self._get( url, args)
        return data

    def getMetadata(self, args={}, params={}):
        """"""
        url = "diagnostics/networkinsight/getMetadata/"
        data = {}

        data = self._get( url, args)
        return data

    def getProtocols(self, args={}, params={}):
        """"""
        url = "diagnostics/networkinsight/getProtocols/"
        data = {}

        data = self._get( url, args)
        return data

    def getServices(self, args={}, params={}):
        """"""
        url = "diagnostics/networkinsight/getServices/"
        data = {}

        data = self._get( url, args)
        return data

class diagnostics_systemhealth(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticssystemhealth API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def getInterfaces(self, args={}, params={}):
        """"""
        url = "diagnostics/systemhealth/getInterfaces/"
        data = {}

        data = self._get( url, args)
        return data

    def getRRDlist(self, args={}, params={}):
        """"""
        url = "diagnostics/systemhealth/getRRDlist/"
        data = {}

        data = self._get( url, args)
        return data

class diagnostics_traffic(client.BaseClient):
    """A client for interacting with the OPNSense's diagnosticstraffic API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def Interface(self, args={}, params={}):
        """"""
        url = "diagnostics/traffic/Interface/"
        data = {}

        data = self._get( url, args)
        return data

    def Top(self, args={}, params={}):
        """"""
        url = "diagnostics/traffic/Top/"
        data = {}

        if "interfaces" not in args.keys():
            return self.log_error("mandatory argument interfaces is missing")
        else:
            url += args.pop("interfaces")+"/"

        data = self._get( url, args)
        return data
