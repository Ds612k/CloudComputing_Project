import boto3
import json

lambda_client = boto3.client('lambda')

response = lambda_client.invoke(
    FunctionName='LogS3UploadsFunction',
    InvocationType='RequestResponse',
    Payload=json.dumps({})
)

print("Lambda response:")
print(response['Payload'].read().decode())
