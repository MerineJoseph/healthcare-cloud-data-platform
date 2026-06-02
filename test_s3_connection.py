import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

bucket_name = os.getenv("S3_BUCKET_NAME")

response = s3.get_bucket_location(Bucket=bucket_name)

print(f"Connected to bucket: {bucket_name}")
print(f"Bucket location: {response['LocationConstraint']}")
