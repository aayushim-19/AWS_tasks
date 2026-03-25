import json
import boto3
import os
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket and file key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Get file metadata from S3
    response = s3.head_object(Bucket=bucket, Key=key)
    
    file_size = response['ContentLength']  # in bytes
    
    # Extract filename and extension
    file_name = os.path.basename(key)
    file_extension = os.path.splitext(file_name)[1]
    
    # Current timestamp
    timestamp = datetime.utcnow().isoformat()
    
    # Logging
    print("---- File Details ----")
    print(f"File Name: {file_name}")
    print(f"File Size: {file_size} bytes")
    print(f"File Extension: {file_extension}")
    print(f"Timestamp (UTC): {timestamp}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }