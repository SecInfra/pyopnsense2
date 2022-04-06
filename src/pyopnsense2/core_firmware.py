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

class Core_Firmware(client.BaseClient):
    """A client for interacting with the OPNSense's CoreFirmware API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def audit(self, args={}, params={}):
        """"""
        url = "core/firmware/audit/"
        data = {}

        data = self._post( url, args)
        return data

    def changelog(self, args={}, params={}):
        """"""
        url = "core/firmware/changelog/"
        data = {}

        if "version" not in args.keys():
            return self.log_error("mandatory argument version is missing")
        else:
            url += args.pop("version")+"/"

        data = self._post( url, args)
        return data

    def details(self, args={}, params={}):
        """"""
        url = "core/firmware/details/"
        data = {}

        if "pkg_name" not in args.keys():
            return self.log_error("mandatory argument pkg_name is missing")
        else:
            url += args.pop("pkg_name")+"/"

        data = self._post( url, args)
        return data

    def getFirmwareConfig(self, args={}, params={}):
        """"""
        url = "core/firmware/getFirmwareConfig/"
        data = {}

        data = self._get( url, args)
        return data

    def getFirmwareOptions(self, args={}, params={}):
        """"""
        url = "core/firmware/getFirmwareOptions/"
        data = {}

        data = self._get( url, args)
        return data

    def info(self, args={}, params={}):
        """"""
        url = "core/firmware/info/"
        data = {}

        data = self._get( url, args)
        return data

    def install(self, args={}, params={}):
        """"""
        url = "core/firmware/install/"
        data = {}

        if "pkg_name" not in args.keys():
            return self.log_error("mandatory argument pkg_name is missing")
        else:
            url += args.pop("pkg_name")+"/"

        data = self._post( url, args)
        return data

    def license(self, args={}, params={}):
        """"""
        url = "core/firmware/license/"
        data = {}

        if "pkg_name" not in args.keys():
            return self.log_error("mandatory argument pkg_name is missing")
        else:
            url += args.pop("pkg_name")+"/"

        data = self._post( url, args)
        return data

    def lock(self, args={}, params={}):
        """"""
        url = "core/firmware/lock/"
        data = {}

        if "pkg_name" not in args.keys():
            return self.log_error("mandatory argument pkg_name is missing")
        else:
            url += args.pop("pkg_name")+"/"

        data = self._post( url, args)
        return data

    def poweroff(self, args={}, params={}):
        """"""
        url = "core/firmware/poweroff/"
        data = {}

        data = self._post( url, args)
        return data

    def reboot(self, args={}, params={}):
        """"""
        url = "core/firmware/reboot/"
        data = {}

        data = self._post( url, args)
        return data

    def reinstall(self, args={}, params={}):
        """"""
        url = "core/firmware/reinstall/"
        data = {}

        if "pkg_name" not in args.keys():
            return self.log_error("mandatory argument pkg_name is missing")
        else:
            url += args.pop("pkg_name")+"/"

        data = self._post( url, args)
        return data

    def remove(self, args={}, params={}):
        """"""
        url = "core/firmware/remove/"
        data = {}

        if "pkg_name" not in args.keys():
            return self.log_error("mandatory argument pkg_name is missing")
        else:
            url += args.pop("pkg_name")+"/"

        data = self._post( url, args)
        return data

    def running(self, args={}, params={}):
        """"""
        url = "core/firmware/running/"
        data = {}

        data = self._get( url, args)
        return data

    def setFirmwareConfig(self, args={}, params={}):
        """"""
        url = "core/firmware/setFirmwareConfig/"
        data = {}

        data = self._post( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "core/firmware/status/"
        data = {}

        data = self._get( url, args)
        return data

    def unlock(self, args={}, params={}):
        """"""
        url = "core/firmware/unlock/"
        data = {}

        if "pkg_name" not in args.keys():
            return self.log_error("mandatory argument pkg_name is missing")
        else:
            url += args.pop("pkg_name")+"/"

        data = self._post( url, args)
        return data

    def update(self, args={}, params={}):
        """"""
        url = "core/firmware/update/"
        data = {}

        data = self._post( url, args)
        return data

    def upgrade(self, args={}, params={}):
        """"""
        url = "core/firmware/upgrade/"
        data = {}

        data = self._post( url, args)
        return data

    def upgradestatus(self, args={}, params={}):
        """"""
        url = "core/firmware/upgradestatus/"
        data = {}

        data = self._get( url, args)
        return data
