# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.organizations.awsserviceeventviacloudtrail.CreateAccountStatus import CreateAccountStatus  # noqa: F401,E501

class ServiceEventDetails(object):


    _types = {
        'createAccountStatus': 'CreateAccountStatus'
    }

    _attribute_map = {
        'createAccountStatus': 'createAccountStatus'
    }

    def __init__(self, createAccountStatus=None):  # noqa: E501
        self._createAccountStatus = None
        self.discriminator = None
        self.createAccountStatus = createAccountStatus


    @property
    def createAccountStatus(self):

        return self._createAccountStatus

    @createAccountStatus.setter
    def createAccountStatus(self, createAccountStatus):


        self._createAccountStatus = createAccountStatus

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
        if issubclass(ServiceEventDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ServiceEventDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

