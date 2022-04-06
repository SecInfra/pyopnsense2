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

class openvpn_export(client.BaseClient):
    """A client for interacting with the OPNSense's openvpnexport API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def accounts(self, args={}, params={}):
        """"""
        url = "openvpn/export/accounts/"
        data = {}

        if "vpnid" not in args.keys():
            return self.log_error("mandatory argument vpnid is missing")
        else:
            url += args.pop("vpnid")+"/"

        data = self._get( url, args)
        return data

    def download(self, args={}, params={}):
        """"""
        url = "openvpn/export/download/"
        data = {}

        if "certref" not in args.keys():
            return self.log_error("mandatory argument certref is missing")
        else:
            url += args.pop("certref")+"/"

        if "vpnid" not in args.keys():
            return self.log_error("mandatory argument vpnid is missing")
        else:
            url += args.pop("vpnid")+"/"

        data = self._post( url, args)
        return data

    def providers(self, args={}, params={}):
        """"""
        url = "openvpn/export/providers/"
        data = {}

        data = self._get( url, args)
        return data

    def storePresets(self, args={}, params={}):
        """"""
        url = "openvpn/export/storePresets/"
        data = {}

        if "vpnid" not in args.keys():
            return self.log_error("mandatory argument vpnid is missing")
        else:
            url += args.pop("vpnid")+"/"

        data = self._post( url, args)
        return data

    def templates(self, args={}, params={}):
        """"""
        url = "openvpn/export/templates/"
        data = {}

        data = self._get( url, args)
        return data

    def validatePresets(self, args={}, params={}):
        """"""
        url = "openvpn/export/validatePresets/"
        data = {}

        if "vpnid" not in args.keys():
            return self.log_error("mandatory argument vpnid is missing")
        else:
            url += args.pop("vpnid")+"/"

        data = self._post( url, args)
        return data
