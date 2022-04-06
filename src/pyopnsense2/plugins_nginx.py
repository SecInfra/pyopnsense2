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

class nginx_bans(client.BaseClient):
    """A client for interacting with the OPNSense's nginxbans API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/www/nginx/src/opnsense/mvc/app/models/OPNsense/Nginx/Nginx.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def delban(self, args={}, params={}):
        """"""
        url = "nginx/bans/delban/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "nginx/bans/get/"
        data = {}

        data = self._get( url, args)
        return data

    def searchban(self, args={}, params={}):
        """"""
        url = "nginx/bans/searchban/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "nginx/bans/set/"
        data = {}

        data = self._get( url, args)
        return data

class nginx_logs(client.BaseClient):
    """A client for interacting with the OPNSense's nginxlogs API.
    for more information on used parameters, see : 

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def accesses(self, args={}, params={}):
        """"""
        url = "nginx/logs/accesses/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def errors(self, args={}, params={}):
        """"""
        url = "nginx/logs/errors/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def stream_accesses(self, args={}, params={}):
        """"""
        url = "nginx/logs/stream_accesses/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def stream_errors(self, args={}, params={}):
        """"""
        url = "nginx/logs/stream_errors/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def tls_handshakes(self, args={}, params={}):
        """"""
        url = "nginx/logs/tls_handshakes/"
        data = {}

        data = self._get( url, args)
        return data

class nginx_service(client.BaseClient):
    """A client for interacting with the OPNSense's nginxservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/www/nginx/src/opnsense/mvc/app/models/OPNsense/Nginx/Nginx.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def reconfigure(self, args={}, params={}):
        """"""
        url = "nginx/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "nginx/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "nginx/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "nginx/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "nginx/service/stop/"
        data = {}

        data = self._get( url, args)
        return data

    def vts(self, args={}, params={}):
        """"""
        url = "nginx/service/vts/"
        data = {}

        data = self._get( url, args)
        return data

class nginx_settings(client.BaseClient):
    """A client for interacting with the OPNSense's nginxsettings API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/www/nginx/src/opnsense/mvc/app/models/OPNsense/Nginx/Nginx.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addcache_path(self, args={}, params={}):
        """"""
        url = "nginx/settings/addcache_path/"
        data = {}

        data = self._post( url, args)
        return data

    def addcredential(self, args={}, params={}):
        """"""
        url = "nginx/settings/addcredential/"
        data = {}

        data = self._post( url, args)
        return data

    def addcustompolicy(self, args={}, params={}):
        """"""
        url = "nginx/settings/addcustompolicy/"
        data = {}

        data = self._post( url, args)
        return data

    def addhttprewrite(self, args={}, params={}):
        """"""
        url = "nginx/settings/addhttprewrite/"
        data = {}

        data = self._post( url, args)
        return data

    def addhttpserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/addhttpserver/"
        data = {}

        data = self._post( url, args)
        return data

    def addipacl(self, args={}, params={}):
        """"""
        url = "nginx/settings/addipacl/"
        data = {}

        data = self._post( url, args)
        return data

    def addlimit_request_connection(self, args={}, params={}):
        """"""
        url = "nginx/settings/addlimit_request_connection/"
        data = {}

        data = self._post( url, args)
        return data

    def addlimit_zone(self, args={}, params={}):
        """"""
        url = "nginx/settings/addlimit_zone/"
        data = {}

        data = self._post( url, args)
        return data

    def addlocation(self, args={}, params={}):
        """"""
        url = "nginx/settings/addlocation/"
        data = {}

        data = self._post( url, args)
        return data

    def addnaxsirule(self, args={}, params={}):
        """"""
        url = "nginx/settings/addnaxsirule/"
        data = {}

        data = self._post( url, args)
        return data

    def addsecurity_header(self, args={}, params={}):
        """"""
        url = "nginx/settings/addsecurity_header/"
        data = {}

        data = self._post( url, args)
        return data

    def addsnifwd(self, args={}, params={}):
        """"""
        url = "nginx/settings/addsnifwd/"
        data = {}

        data = self._post( url, args)
        return data

    def addstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/addstreamserver/"
        data = {}

        data = self._post( url, args)
        return data

    def addsyslog_target(self, args={}, params={}):
        """"""
        url = "nginx/settings/addsyslog_target/"
        data = {}

        data = self._post( url, args)
        return data

    def addtls_fingerprint(self, args={}, params={}):
        """"""
        url = "nginx/settings/addtls_fingerprint/"
        data = {}

        data = self._post( url, args)
        return data

    def addupstream(self, args={}, params={}):
        """"""
        url = "nginx/settings/addupstream/"
        data = {}

        data = self._post( url, args)
        return data

    def addupstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/addupstreamserver/"
        data = {}

        data = self._post( url, args)
        return data

    def adduserlist(self, args={}, params={}):
        """"""
        url = "nginx/settings/adduserlist/"
        data = {}

        data = self._post( url, args)
        return data

    def delcache_path(self, args={}, params={}):
        """"""
        url = "nginx/settings/delcache_path/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delcredential(self, args={}, params={}):
        """"""
        url = "nginx/settings/delcredential/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delcustompolicy(self, args={}, params={}):
        """"""
        url = "nginx/settings/delcustompolicy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delhttprewrite(self, args={}, params={}):
        """"""
        url = "nginx/settings/delhttprewrite/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delhttpserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/delhttpserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delipacl(self, args={}, params={}):
        """"""
        url = "nginx/settings/delipacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def dellimit_request_connection(self, args={}, params={}):
        """"""
        url = "nginx/settings/dellimit_request_connection/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def dellimit_zone(self, args={}, params={}):
        """"""
        url = "nginx/settings/dellimit_zone/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def dellocation(self, args={}, params={}):
        """"""
        url = "nginx/settings/dellocation/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delnaxsirule(self, args={}, params={}):
        """"""
        url = "nginx/settings/delnaxsirule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delsecurity_header(self, args={}, params={}):
        """"""
        url = "nginx/settings/delsecurity_header/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delsnifwd(self, args={}, params={}):
        """"""
        url = "nginx/settings/delsnifwd/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/delstreamserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delsyslog_target(self, args={}, params={}):
        """"""
        url = "nginx/settings/delsyslog_target/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def deltls_fingerprint(self, args={}, params={}):
        """"""
        url = "nginx/settings/deltls_fingerprint/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delupstream(self, args={}, params={}):
        """"""
        url = "nginx/settings/delupstream/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def delupstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/delupstreamserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def deluserlist(self, args={}, params={}):
        """"""
        url = "nginx/settings/deluserlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def downloadrules(self, args={}, params={}):
        """"""
        url = "nginx/settings/downloadrules/"
        data = {}

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "nginx/settings/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getcache_path(self, args={}, params={}):
        """"""
        url = "nginx/settings/getcache_path/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getcredential(self, args={}, params={}):
        """"""
        url = "nginx/settings/getcredential/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getcustompolicy(self, args={}, params={}):
        """"""
        url = "nginx/settings/getcustompolicy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def gethttprewrite(self, args={}, params={}):
        """"""
        url = "nginx/settings/gethttprewrite/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def gethttpserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/gethttpserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getipacl(self, args={}, params={}):
        """"""
        url = "nginx/settings/getipacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getlimit_request_connection(self, args={}, params={}):
        """"""
        url = "nginx/settings/getlimit_request_connection/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getlimit_zone(self, args={}, params={}):
        """"""
        url = "nginx/settings/getlimit_zone/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getlocation(self, args={}, params={}):
        """"""
        url = "nginx/settings/getlocation/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getnaxsirule(self, args={}, params={}):
        """"""
        url = "nginx/settings/getnaxsirule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getsecurity_header(self, args={}, params={}):
        """"""
        url = "nginx/settings/getsecurity_header/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getsnifwd(self, args={}, params={}):
        """"""
        url = "nginx/settings/getsnifwd/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/getstreamserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getsyslog_target(self, args={}, params={}):
        """"""
        url = "nginx/settings/getsyslog_target/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def gettls_fingerprint(self, args={}, params={}):
        """"""
        url = "nginx/settings/gettls_fingerprint/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getupstream(self, args={}, params={}):
        """"""
        url = "nginx/settings/getupstream/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getupstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/getupstreamserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def getuserlist(self, args={}, params={}):
        """"""
        url = "nginx/settings/getuserlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchcache_path(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchcache_path/"
        data = {}

        data = self._get( url, args)
        return data

    def searchcredential(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchcredential/"
        data = {}

        data = self._get( url, args)
        return data

    def searchcustompolicy(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchcustompolicy/"
        data = {}

        data = self._get( url, args)
        return data

    def searchhttprewrite(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchhttprewrite/"
        data = {}

        data = self._get( url, args)
        return data

    def searchhttpserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchhttpserver/"
        data = {}

        data = self._get( url, args)
        return data

    def searchipacl(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchipacl/"
        data = {}

        data = self._get( url, args)
        return data

    def searchlimit_request_connection(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchlimit_request_connection/"
        data = {}

        data = self._get( url, args)
        return data

    def searchlimit_zone(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchlimit_zone/"
        data = {}

        data = self._get( url, args)
        return data

    def searchlocation(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchlocation/"
        data = {}

        data = self._get( url, args)
        return data

    def searchnaxsirule(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchnaxsirule/"
        data = {}

        data = self._get( url, args)
        return data

    def searchsecurity_header(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchsecurity_header/"
        data = {}

        data = self._get( url, args)
        return data

    def searchsnifwd(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchsnifwd/"
        data = {}

        data = self._get( url, args)
        return data

    def searchstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchstreamserver/"
        data = {}

        data = self._get( url, args)
        return data

    def searchsyslog_target(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchsyslog_target/"
        data = {}

        data = self._get( url, args)
        return data

    def searchtls_fingerprint(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchtls_fingerprint/"
        data = {}

        data = self._get( url, args)
        return data

    def searchupstream(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchupstream/"
        data = {}

        data = self._get( url, args)
        return data

    def searchupstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchupstreamserver/"
        data = {}

        data = self._get( url, args)
        return data

    def searchuserlist(self, args={}, params={}):
        """"""
        url = "nginx/settings/searchuserlist/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "nginx/settings/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setcache_path(self, args={}, params={}):
        """"""
        url = "nginx/settings/setcache_path/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setcredential(self, args={}, params={}):
        """"""
        url = "nginx/settings/setcredential/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setcustompolicy(self, args={}, params={}):
        """"""
        url = "nginx/settings/setcustompolicy/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def sethttprewrite(self, args={}, params={}):
        """"""
        url = "nginx/settings/sethttprewrite/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def sethttpserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/sethttpserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setipacl(self, args={}, params={}):
        """"""
        url = "nginx/settings/setipacl/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setlimit_request_connection(self, args={}, params={}):
        """"""
        url = "nginx/settings/setlimit_request_connection/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setlimit_zone(self, args={}, params={}):
        """"""
        url = "nginx/settings/setlimit_zone/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setlocation(self, args={}, params={}):
        """"""
        url = "nginx/settings/setlocation/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setnaxsirule(self, args={}, params={}):
        """"""
        url = "nginx/settings/setnaxsirule/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setsecurity_header(self, args={}, params={}):
        """"""
        url = "nginx/settings/setsecurity_header/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setsnifwd(self, args={}, params={}):
        """"""
        url = "nginx/settings/setsnifwd/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/setstreamserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setsyslog_target(self, args={}, params={}):
        """"""
        url = "nginx/settings/setsyslog_target/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def settls_fingerprint(self, args={}, params={}):
        """"""
        url = "nginx/settings/settls_fingerprint/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setupstream(self, args={}, params={}):
        """"""
        url = "nginx/settings/setupstream/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setupstreamserver(self, args={}, params={}):
        """"""
        url = "nginx/settings/setupstreamserver/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def setuserlist(self, args={}, params={}):
        """"""
        url = "nginx/settings/setuserlist/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data
