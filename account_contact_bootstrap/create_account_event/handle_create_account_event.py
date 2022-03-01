## Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
## SPDX-License-Identifier: MIT-0
import json
import logging
import os
from botocore.exceptions import ClientError

from .helper import AccountHelper
from schema.aws.organizations.awsserviceeventviacloudtrail import Marshaller
from schema.aws.organizations.awsserviceeventviacloudtrail import AWSEvent
from schema.aws.controltower.awsserviceeventviacloudtrail import Marshaller as ctMarshaller
from schema.aws.controltower.awsserviceeventviacloudtrail import AWSEvent as ctAWSEvent


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def check_propagate_tags(tag_list, propagate_tag_name):
    tag_names = [tag["Key"] for tag in tag_list]
    return (tag_names and propagate_tag_name in tag_names)
    
def lambda_handler(event, context):
    status_code = 200
    message ='function complete'
    billing_email = os.environ["BILLING_EMAIL"]
    security_email = os.environ["SECURITY_EMAIL"]
    operations_email =  os.environ["OPERATIONS_EMAIL"]
    billing_contact_name = os.environ["BILLING_CONTACT_NAME"]
    security_contact_name = os.environ["SECURITY_CONTACT_NAME"]
    operations_contact_name =  os.environ["OPERATIONS_CONTACT_NAME"]
    billing_contact_title = os.environ["BILLING_CONTACT_TITLE"]
    security_contact_title = os.environ["SECURITY_CONTACT_TITLE"]
    operations_contact_title = os.environ["OPERATIONS_CONTACT_TITLE"]
    billing_contact_phone = os.environ["BILLING_CONTACT_PHONE"]
    security_contact_phone = os.environ["SECURITY_CONTACT_PHONE"]
    operations_contact_phone = os.environ["OPERATIONS_CONTACT_PHONE"]


    new_account_id=''
    if event["source"] == "aws.organizations":
        aws_event:AWSEvent = Marshaller.unmarshall(event, AWSEvent)
        new_account_id = aws_event.detail.serviceEventDetails.createAccountStatus.accountId
    else:
        aws_event:ctAWSEvent = ctMarshaller.unmarshall(event, ctAWSEvent)
        new_account_id = aws_event.detail.serviceEventDetails.createManagedAccountStatus._account.accountId
    try:
        AccountHelper.update_account_contact(new_account_id,billing_email,"BILLING",billing_contact_name,billing_contact_title,billing_contact_phone)
        logger.info("Updated Billing alternate Contact")
        AccountHelper.update_account_contact(new_account_id,security_email,"SECURITY",security_contact_name,security_contact_title,security_contact_phone)
        logger.info("Updated Security alternate Contact")
        AccountHelper.update_account_contact(new_account_id,operations_email,"OPERATIONS",operations_contact_name,operations_contact_title,operations_contact_phone)
        logger.info("Updated Operations alternate Contact")
    except ClientError as error:
        logger.warn(error.response['Error']['Message'])
        status_code = 500
        message = error.response['Error']['Message']
    except Exception as error:
        status_code = 500
        message = "Unexpected Error occured"
    #Return event for further processing
    return {
        'statusCode': status_code,
        'body': json.dumps(message)
    }
