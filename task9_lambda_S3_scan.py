import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = "your-bucket-name"  # 👈 change this

def lambda_handler(event, context):
    now = datetime.now(timezone.utc)
    one_hour_ago = now - timedelta(hours=1)

    print(f"Scanning bucket: {BUCKET_NAME}")
    print(f"Time window: {one_hour_ago} to {now}")

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in response:
        print("No files found.")
        return

    for obj in response['Contents']:
        last_modified = obj['LastModified']

        if last_modified >= one_hour_ago:
            print(f"New file: {obj['Key']} | Uploaded at: {last_modified}")
