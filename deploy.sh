#!/bin/bash
set -eo pipefail
if [[ $# -lt 1 ]] ; then
     echo "Please specify the region as the arguement eg: ./deploy.sh us-east-1"
     exit
else
     REGION=$1
fi
ARTIFACT_BUCKET=$(cat bucket-name.txt)
TEMPLATE=aws-account-contact-bootstrap-template.yaml
PROFILE=$(cat profile.txt)
sam build -t $TEMPLATE
cd .aws-sam/build

sam package --debug  --profile $PROFILE --region $REGION --s3-bucket $ARTIFACT_BUCKET --output-template-file aws-account-contact-bootstrap-template-cf.yml
sam deploy --debug --profile $PROFILE --region $REGION --template-file aws-account-contact-bootstrap-template-cf.yml --stack-name aws-account-contact-bootstrap --capabilities CAPABILITY_NAMED_IAM
