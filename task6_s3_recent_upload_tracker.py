import boto3
from datetime import datetime, timedelta, timezone

# Initialize S3 client
s3 = boto3.client('s3')

# Replace with your bucket name
BUCKET_NAME = "aayushi-trail-bucket"

def lambda_handler(event, context):
    # Get current time and time 60 minutes ago
    now = datetime.now(timezone.utc)
    one_hour_ago = now - timedelta(hours=1)
    
    # List all objects in the bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    if 'Contents' in response:
        recent_files = []
        for obj in response['Contents']:
            # Check if object was created in the last hour
            if obj['LastModified'] >= one_hour_ago:
                recent_files.append(obj['Key'])
        
        if recent_files:
            print(f"Files uploaded in the last 60 minutes: {recent_files}")
        else:
            print("No files uploaded in the last 60 minutes.")
    else:
        print("Bucket is empty.")