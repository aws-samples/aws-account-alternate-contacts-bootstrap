# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class CreateAccountStatus(object):


    _types = {
        'accountId': 'str',
        'accountName': 'str',
        'completedTimestamp': 'str',
        'id': 'str',
        'state': 'str',
        'requestedTimestamp': 'str'
    }

    _attribute_map = {
        'accountId': 'accountId',
        'accountName': 'accountName',
        'completedTimestamp': 'completedTimestamp',
        'id': 'id',
        'state': 'state',
        'requestedTimestamp': 'requestedTimestamp'
    }

    def __init__(self, accountId=None, accountName=None, completedTimestamp=None, id=None, state=None, requestedTimestamp=None):  # noqa: E501
        self._accountId = None
        self._accountName = None
        self._completedTimestamp = None
        self._id = None
        self._state = None
        self._requestedTimestamp = None
        self.discriminator = None
        self.accountId = accountId
        self.accountName = accountName
        self.completedTimestamp = completedTimestamp
        self.id = id
        self.state = state
        self.requestedTimestamp = requestedTimestamp


    @property
    def accountId(self):

        return self._accountId

    @accountId.setter
    def accountId(self, accountId):


        self._accountId = accountId


    @property
    def accountName(self):

        return self._accountName

    @accountName.setter
    def accountName(self, accountName):


        self._accountName = accountName


    @property
    def completedTimestamp(self):

        return self._completedTimestamp

    @completedTimestamp.setter
    def completedTimestamp(self, completedTimestamp):


        self._completedTimestamp = completedTimestamp


    @property
    def id(self):

        return self._id

    @id.setter
    def id(self, id):


        self._id = id


    @property
    def state(self):

        return self._state

    @state.setter
    def state(self, state):


        self._state = state


    @property
    def requestedTimestamp(self):

        return self._requestedTimestamp

    @requestedTimestamp.setter
    def requestedTimestamp(self, requestedTimestamp):


        self._requestedTimestamp = requestedTimestamp

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
        if issubclass(CreateAccountStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CreateAccountStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

