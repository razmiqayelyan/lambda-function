# Lambda S3 Bucket Creator

This AWS Lambda function creates an S3 bucket with a unique name based on the current timestamp.

## Features
- Automatically generates a unique bucket name.
- Creates the bucket in a specified AWS region.

## Requirements
- AWS account with S3 permissions.
- IAM role with the following policies:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:CreateBucket",
          "s3:PutBucketAcl",
          "s3:PutBucketPolicy"
        ],
        "Resource": "arn:aws:s3:::*"
      }
    ]
  }
