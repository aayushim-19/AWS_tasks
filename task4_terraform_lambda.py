def lambda_handler(event, context):
    print("Hello from Terraform")
    return {
        "statusCode": 200,
        "body": "Hello from Terraform"
    }