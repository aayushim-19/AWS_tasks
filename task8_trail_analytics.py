import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    response = s3.list_objects_v2(
        Bucket='analytics-input-data'
    )
    
    for obj in response.get('Contents', []):
        print(obj['Key'])
        
    return "S3 Access Working ✅"
