# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.controltower.awsserviceeventviacloudtrail.Account import Account  # noqa: F401,E501
from schema.aws.controltower.awsserviceeventviacloudtrail.OrganizationalUnit import OrganizationalUnit  # noqa: F401,E501

class CreateManagedAccountStatus(object):


    _types = {
        'account': 'Account',
        'organizationalUnit': 'OrganizationalUnit',
        'completedTimestamp': 'str',
        'message': 'str',
        'requestedTimestamp': 'str',
        'state': 'str'
    }

    _attribute_map = {
        'account': 'account',
        'organizationalUnit': 'organizationalUnit',
        'completedTimestamp': 'completedTimestamp',
        'message': 'message',
        'requestedTimestamp': 'requestedTimestamp',
        'state': 'state'
    }

    def __init__(self, account=None, organizationalUnit=None, completedTimestamp=None, message=None, requestedTimestamp=None, state=None):  # noqa: E501
        self._account = None
        self._organizationalUnit = None
        self._completedTimestamp = None
        self._message = None
        self._requestedTimestamp = None
        self._state = None
        self.discriminator = None
        self.account = account
        self.organizationalUnit = organizationalUnit
        self.completedTimestamp = completedTimestamp
        self.message = message
        self.requestedTimestamp = requestedTimestamp
        self.state = state


    @property
    def account(self):

        return self._account

    @account.setter
    def account(self, account):


        self._account = account


    @property
    def organizationalUnit(self):

        return self._organizationalUnit

    @organizationalUnit.setter
    def organizationalUnit(self, organizationalUnit):


        self._organizationalUnit = organizationalUnit


    @property
    def completedTimestamp(self):

        return self._completedTimestamp

    @completedTimestamp.setter
    def completedTimestamp(self, completedTimestamp):


        self._completedTimestamp = completedTimestamp


    @property
    def message(self):

        return self._message

    @message.setter
    def message(self, message):


        self._message = message


    @property
    def requestedTimestamp(self):

        return self._requestedTimestamp

    @requestedTimestamp.setter
    def requestedTimestamp(self, requestedTimestamp):


        self._requestedTimestamp = requestedTimestamp


    @property
    def state(self):

        return self._state

    @state.setter
    def state(self, state):


        self._state = state

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateManagedAccountStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CreateManagedAccountStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

