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

class postfix_address(client.BaseClient):
    """A client for interacting with the OPNSense's postfixaddress API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Address.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addAddress(self, args={}, params={}):
        """"""
        url = "postfix/address/addAddress/"
        data = {}

        data = self._post( url, args)
        return data

    def delAddress(self, args={}, params={}):
        """"""
        url = "postfix/address/delAddress/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/address/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getAddress(self, args={}, params={}):
        """"""
        url = "postfix/address/getAddress/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchAddress(self, args={}, params={}):
        """"""
        url = "postfix/address/searchAddress/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/address/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setAddress(self, args={}, params={}):
        """"""
        url = "postfix/address/setAddress/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleAddress(self, args={}, params={}):
        """"""
        url = "postfix/address/toggleAddress/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_antispam(client.BaseClient):
    """A client for interacting with the OPNSense's postfixantispam API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Antispam.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "postfix/antispam/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/antispam/set/"
        data = {}

        data = self._get( url, args)
        return data

class postfix_domain(client.BaseClient):
    """A client for interacting with the OPNSense's postfixdomain API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Domain.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addDomain(self, args={}, params={}):
        """"""
        url = "postfix/domain/addDomain/"
        data = {}

        data = self._post( url, args)
        return data

    def delDomain(self, args={}, params={}):
        """"""
        url = "postfix/domain/delDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/domain/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getDomain(self, args={}, params={}):
        """"""
        url = "postfix/domain/getDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchDomain(self, args={}, params={}):
        """"""
        url = "postfix/domain/searchDomain/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/domain/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setDomain(self, args={}, params={}):
        """"""
        url = "postfix/domain/setDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleDomain(self, args={}, params={}):
        """"""
        url = "postfix/domain/toggleDomain/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_general(client.BaseClient):
    """A client for interacting with the OPNSense's postfixgeneral API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get(self, args={}, params={}):
        """"""
        url = "postfix/general/get/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/general/set/"
        data = {}

        data = self._get( url, args)
        return data

class postfix_headerchecks(client.BaseClient):
    """A client for interacting with the OPNSense's postfixheaderchecks API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Headerchecks.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addHeadercheck(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/addHeadercheck/"
        data = {}

        data = self._post( url, args)
        return data

    def delHeadercheck(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/delHeadercheck/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getHeadercheck(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/getHeadercheck/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchHeaderchecks(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/searchHeaderchecks/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setHeadercheck(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/setHeadercheck/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleHeadercheck(self, args={}, params={}):
        """"""
        url = "postfix/headerchecks/toggleHeadercheck/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_recipient(client.BaseClient):
    """A client for interacting with the OPNSense's postfixrecipient API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Recipient.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addRecipient(self, args={}, params={}):
        """"""
        url = "postfix/recipient/addRecipient/"
        data = {}

        data = self._post( url, args)
        return data

    def delRecipient(self, args={}, params={}):
        """"""
        url = "postfix/recipient/delRecipient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/recipient/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getRecipient(self, args={}, params={}):
        """"""
        url = "postfix/recipient/getRecipient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchRecipient(self, args={}, params={}):
        """"""
        url = "postfix/recipient/searchRecipient/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/recipient/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setRecipient(self, args={}, params={}):
        """"""
        url = "postfix/recipient/setRecipient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRecipient(self, args={}, params={}):
        """"""
        url = "postfix/recipient/toggleRecipient/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_recipientbcc(client.BaseClient):
    """A client for interacting with the OPNSense's postfixrecipientbcc API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Recipientbcc.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addRecipientbcc(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/addRecipientbcc/"
        data = {}

        data = self._post( url, args)
        return data

    def delRecipientbcc(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/delRecipientbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getRecipientbcc(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/getRecipientbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchRecipientbcc(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/searchRecipientbcc/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setRecipientbcc(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/setRecipientbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleRecipientbcc(self, args={}, params={}):
        """"""
        url = "postfix/recipientbcc/toggleRecipientbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_sender(client.BaseClient):
    """A client for interacting with the OPNSense's postfixsender API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Sender.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addSender(self, args={}, params={}):
        """"""
        url = "postfix/sender/addSender/"
        data = {}

        data = self._post( url, args)
        return data

    def delSender(self, args={}, params={}):
        """"""
        url = "postfix/sender/delSender/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/sender/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getSender(self, args={}, params={}):
        """"""
        url = "postfix/sender/getSender/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchSender(self, args={}, params={}):
        """"""
        url = "postfix/sender/searchSender/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/sender/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setSender(self, args={}, params={}):
        """"""
        url = "postfix/sender/setSender/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleSender(self, args={}, params={}):
        """"""
        url = "postfix/sender/toggleSender/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_senderbcc(client.BaseClient):
    """A client for interacting with the OPNSense's postfixsenderbcc API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Senderbcc.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addSenderbcc(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/addSenderbcc/"
        data = {}

        data = self._post( url, args)
        return data

    def delSenderbcc(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/delSenderbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getSenderbcc(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/getSenderbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchSenderbcc(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/searchSenderbcc/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setSenderbcc(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/setSenderbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleSenderbcc(self, args={}, params={}):
        """"""
        url = "postfix/senderbcc/toggleSenderbcc/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_sendercanonical(client.BaseClient):
    """A client for interacting with the OPNSense's postfixsendercanonical API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Sendercanonical.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def addSendercanonical(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/addSendercanonical/"
        data = {}

        data = self._post( url, args)
        return data

    def delSendercanonical(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/delSendercanonical/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def get(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/get/"
        data = {}

        data = self._get( url, args)
        return data

    def getSendercanonical(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/getSendercanonical/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._get( url, args)
        return data

    def searchSendercanonical(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/searchSendercanonical/"
        data = {}

        data = self._get( url, args)
        return data

    def set(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/set/"
        data = {}

        data = self._get( url, args)
        return data

    def setSendercanonical(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/setSendercanonical/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

    def toggleSendercanonical(self, args={}, params={}):
        """"""
        url = "postfix/sendercanonical/toggleSendercanonical/"
        data = {}

        if "uuid" not in args.keys():
            return self.log_error("mandatory argument uuid is missing")
        else:
            url += args.pop("uuid")+"/"

        data = self._post( url, args)
        return data

class postfix_service(client.BaseClient):
    """A client for interacting with the OPNSense's postfixservice API.
    for more information on used parameters, see : ['https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/General.xml']

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def checkrspamd(self, args={}, params={}):
        """"""
        url = "postfix/service/checkrspamd/"
        data = {}

        data = self._get( url, args)
        return data

    def reconfigure(self, args={}, params={}):
        """"""
        url = "postfix/service/reconfigure/"
        data = {}

        data = self._get( url, args)
        return data

    def restart(self, args={}, params={}):
        """"""
        url = "postfix/service/restart/"
        data = {}

        data = self._get( url, args)
        return data

    def start(self, args={}, params={}):
        """"""
        url = "postfix/service/start/"
        data = {}

        data = self._get( url, args)
        return data

    def status(self, args={}, params={}):
        """"""
        url = "postfix/service/status/"
        data = {}

        data = self._get( url, args)
        return data

    def stop(self, args={}, params={}):
        """"""
        url = "postfix/service/stop/"
        data = {}

        data = self._get( url, args)
        return data
