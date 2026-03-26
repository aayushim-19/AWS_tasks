provider "aws" {
  region = "ap-south-1"
}

# IAM Role
resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Attach basic policy
resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# -----------------------
# Pandas Layer
# -----------------------
resource "aws_lambda_layer_version" "pandas_layer" {
  filename   = "../layers/pandas_layer/pandas_layer.zip"
  layer_name = "pandas-layer"

  compatible_runtimes = ["python3.9"]
}

# -----------------------
# Utils Layer
# -----------------------
resource "aws_lambda_layer_version" "utils_layer" {
  filename   = "../layers/utils_layer/utils_layer.zip"
  layer_name = "utils-layer"

  compatible_runtimes = ["python3.9"]
}

# -----------------------
# Lambda Function
# -----------------------
resource "aws_lambda_function" "clean_lambda" {
  filename         = "../lambda/lambda_function.zip"
  function_name    = "aayushi-file-cleaner"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.9"

  layers = [
    aws_lambda_layer_version.pandas_layer.arn,
    aws_lambda_layer_version.utils_layer.arn
  ]
}