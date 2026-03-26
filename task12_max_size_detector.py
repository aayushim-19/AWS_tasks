import json
import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get MAX_SIZE from environment variable
    max_size = int(os.environ.get("MAX_SIZE", 0))

    # Get bucket and file key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get object metadata (includes size)
    response = s3.head_object(Bucket=bucket, Key=key)
    file_size = response['ContentLength']

    print(f"File: {key}")
    print(f"File size: {file_size} bytes")
    print(f"Max allowed size: {max_size} bytes")

    # Compare file size with MAX_SIZE
    if file_size > max_size:
        print("❌ File exceeds MAX_SIZE limit")
    else:
        print("✅ File is within allowed size")

    return {
        "statusCode": 200,
        "body": json.dumps("Size check completed")
    }