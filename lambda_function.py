import boto3
import os
import time

def lambda_handler(event, context):
    # Set the default AWS region
    AWS_DEFAULT_REGION = "eu-west-1"
    os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

    # Generate a unique bucket name
    bucket_name = "lambda-created-me-on-" + str(int(time.time()))

    # Initialize the S3 resource
    myS3 = boto3.resource('s3')

    try:
        # Create the bucket
        results = myS3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': AWS_DEFAULT_REGION}
        )

        # Log success and return a response
        print(f"<h1><font color='green'>S3 Bucket Created Successfully:</font></h1><br><br>{bucket_name}")
        return {
            'statusCode': 200,
            'body': f"<h1><font color='green'>S3 Bucket Created Successfully:</font></h1><br><br>{bucket_name}"
        }
    except Exception as e:
        # Log error and return an error response
        print("<h1><font color='red'>Error!</font></h1><br><br>")
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'body': f"<h1><font color='red'>Error!</font></h1><br><br>Exception: {e}"
        }
