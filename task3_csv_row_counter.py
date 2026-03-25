import json
import boto3
import csv

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("FULL EVENT:", event)   # 👈 DEBUG LINE

    try:
        # Get bucket and file name
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        print(f"Bucket: {bucket}")
        print(f"Key: {key}")

        # Read file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8').splitlines()
        
        # Read CSV
        csv_reader = csv.reader(content)
        row_count = sum(1 for row in csv_reader)
        
        print(f"File: {key}")
        print(f"Total Rows: {row_count}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Row count: {row_count}")
        }

    except Exception as e:
        print("ERROR:", str(e))   # 👈 VERY IMPORTANT
        raise e