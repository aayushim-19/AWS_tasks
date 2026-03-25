import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['bucket']
    file_key = event['key']

    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response['Body'].read().decode('utf-8')

    lines = content.splitlines()
    line_count = len(lines)

    return {
        'statusCode': 200,
        'line_count': line_count
    }