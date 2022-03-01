# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class OrganizationalUnit(object):


    _types = {
        'organizationalUnitId': 'str',
        'organizationalUnitName': 'str'
    }

    _attribute_map = {
        'organizationalUnitId': 'organizationalUnitId',
        'organizationalUnitName': 'organizationalUnitName'
    }

    def __init__(self, organizationalUnitId=None, organizationalUnitName=None):  # noqa: E501
        self._organizationalUnitId = None
        self._organizationalUnitName = None
        self.discriminator = None
        self.organizationalUnitId = organizationalUnitId
        self.organizationalUnitName = organizationalUnitName


    @property
    def organizationalUnitId(self):

        return self._organizationalUnitId

    @organizationalUnitId.setter
    def organizationalUnitId(self, organizationalUnitId):


        self._organizationalUnitId = organizationalUnitId


    @property
    def organizationalUnitName(self):

        return self._organizationalUnitName

    @organizationalUnitName.setter
    def organizationalUnitName(self, organizationalUnitName):


        self._organizationalUnitName = organizationalUnitName

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
        if issubclass(OrganizationalUnit, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, OrganizationalUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

