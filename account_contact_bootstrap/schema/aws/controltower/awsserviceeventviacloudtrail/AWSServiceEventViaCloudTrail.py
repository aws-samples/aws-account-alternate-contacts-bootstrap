# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.controltower.awsserviceeventviacloudtrail.ServiceEventDetails import ServiceEventDetails  # noqa: F401,E501
from schema.aws.controltower.awsserviceeventviacloudtrail.UserIdentity import UserIdentity  # noqa: F401,E501

class AWSServiceEventViaCloudTrail(object):


    _types = {
        'serviceEventDetails': 'ServiceEventDetails',
        'userIdentity': 'UserIdentity',
        'awsRegion': 'str',
        'eventID': 'str',
        'eventName': 'str',
        'eventSource': 'str',
        'eventTime': 'datetime',
        'eventType': 'str',
        'eventVersion': 'str',
        'readOnly': 'bool',
        'sourceIPAddress': 'str',
        'userAgent': 'str'
    }

    _attribute_map = {
        'serviceEventDetails': 'serviceEventDetails',
        'userIdentity': 'userIdentity',
        'awsRegion': 'awsRegion',
        'eventID': 'eventID',
        'eventName': 'eventName',
        'eventSource': 'eventSource',
        'eventTime': 'eventTime',
        'eventType': 'eventType',
        'eventVersion': 'eventVersion',
        'readOnly': 'readOnly',
        'sourceIPAddress': 'sourceIPAddress',
        'userAgent': 'userAgent'
    }

    def __init__(self, serviceEventDetails=None, userIdentity=None, awsRegion=None, eventID=None, eventName=None, eventSource=None, eventTime=None, eventType=None, eventVersion=None, readOnly=None, sourceIPAddress=None, userAgent=None):  # noqa: E501
        self._serviceEventDetails = None
        self._userIdentity = None
        self._awsRegion = None
        self._eventID = None
        self._eventName = None
        self._eventSource = None
        self._eventTime = None
        self._eventType = None
        self._eventVersion = None
        self._readOnly = None
        self._sourceIPAddress = None
        self._userAgent = None
        self.discriminator = None
        self.serviceEventDetails = serviceEventDetails
        self.userIdentity = userIdentity
        self.awsRegion = awsRegion
        self.eventID = eventID
        self.eventName = eventName
        self.eventSource = eventSource
        self.eventTime = eventTime
        self.eventType = eventType
        self.eventVersion = eventVersion
        self.readOnly = readOnly
        self.sourceIPAddress = sourceIPAddress
        self.userAgent = userAgent


    @property
    def serviceEventDetails(self):

        return self._serviceEventDetails

    @serviceEventDetails.setter
    def serviceEventDetails(self, serviceEventDetails):


        self._serviceEventDetails = serviceEventDetails


    @property
    def userIdentity(self):

        return self._userIdentity

    @userIdentity.setter
    def userIdentity(self, userIdentity):


        self._userIdentity = userIdentity


    @property
    def awsRegion(self):

        return self._awsRegion

    @awsRegion.setter
    def awsRegion(self, awsRegion):


        self._awsRegion = awsRegion


    @property
    def eventID(self):

        return self._eventID

    @eventID.setter
    def eventID(self, eventID):


        self._eventID = eventID


    @property
    def eventName(self):

        return self._eventName

    @eventName.setter
    def eventName(self, eventName):


        self._eventName = eventName


    @property
    def eventSource(self):

        return self._eventSource

    @eventSource.setter
    def eventSource(self, eventSource):


        self._eventSource = eventSource


    @property
    def eventTime(self):

        return self._eventTime

    @eventTime.setter
    def eventTime(self, eventTime):


        self._eventTime = eventTime


    @property
    def eventType(self):

        return self._eventType

    @eventType.setter
    def eventType(self, eventType):


        self._eventType = eventType


    @property
    def eventVersion(self):

        return self._eventVersion

    @eventVersion.setter
    def eventVersion(self, eventVersion):


        self._eventVersion = eventVersion


    @property
    def readOnly(self):

        return self._readOnly

    @readOnly.setter
    def readOnly(self, readOnly):


        self._readOnly = readOnly


    @property
    def sourceIPAddress(self):

        return self._sourceIPAddress

    @sourceIPAddress.setter
    def sourceIPAddress(self, sourceIPAddress):


        self._sourceIPAddress = sourceIPAddress


    @property
    def userAgent(self):

        return self._userAgent

    @userAgent.setter
    def userAgent(self, userAgent):


        self._userAgent = userAgent

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
        if issubclass(AWSServiceEventViaCloudTrail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AWSServiceEventViaCloudTrail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

