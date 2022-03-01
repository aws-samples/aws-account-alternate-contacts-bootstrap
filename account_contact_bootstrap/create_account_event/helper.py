## Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
## SPDX-License-Identifier: MIT-0

import boto3
from botocore.client import Config
import os
import time

class AwsHelper:
    def getClient(self, name, awsRegion=None):
        config = Config(
            retries = {
                'max_attempts': 5,
                'mode': 'standard'
            }
        )
        if(awsRegion):
            return boto3.client(name, region_name=awsRegion, config=config)
        else:
            return boto3.client(name, config=config)

    def getResource(self, name, awsRegion=None):
        config = Config(
            retries = dict(
                max_attempts = 6
            )
        )

        if(awsRegion):
            return boto3.resource(name, region_name=awsRegion, config=config)
        else:
            return boto3.resource(name, config=config)

class AccountHelper:
   
    @staticmethod
    def update_account_contact(account_id, email,type,name,title,phone ):
        account_client = AwsHelper().getClient('account')
        response = account_client.put_alternate_contact(
            AccountId=account_id,
            AlternateContactType=type,
            EmailAddress=email,
            Name=name,
            PhoneNumber=phone,
            Title=title
        )
        return response   


