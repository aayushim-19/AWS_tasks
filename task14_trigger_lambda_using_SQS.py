import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['bucket']
    source_key = event['key']

    dest = event['destination']
    dest_bucket, dest_key = dest.split('/', 1)

    # Copy file
    s3.copy_object(
        Bucket=dest_bucket,
        CopySource={'Bucket': source_bucket, 'Key': source_key},
        Key=dest_key
    )

    # Delete original file (optional)
    s3.delete_object(Bucket=source_bucket, Key=source_key)

    return {
        "status": "file moved",
        "destination": dest
    }