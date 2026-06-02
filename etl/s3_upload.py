import os
from pathlib import Path

import boto3
from dotenv import load_dotenv


load_dotenv()

RAW_DATA_DIR = Path("data/raw")

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


def get_s3_client():
    return boto3.client(
        "s3",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )


def upload_file_to_s3(local_file_path: Path, s3_key: str) -> None:
    s3_client = get_s3_client()

    s3_client.upload_file(
        Filename=str(local_file_path),
        Bucket=S3_BUCKET_NAME,
        Key=s3_key,
    )

    print(f"Uploaded {local_file_path} to s3://{S3_BUCKET_NAME}/{s3_key}")


def upload_raw_files() -> None:
    files = {
        "admissions.csv": "raw/admissions/admissions.csv",
        "bed_occupancy.csv": "raw/bed_occupancy/bed_occupancy.csv",
        "theatre_bookings.csv": "raw/theatre_bookings/theatre_bookings.csv",
    }

    for file_name, s3_key in files.items():
        local_file_path = RAW_DATA_DIR / file_name

        if not local_file_path.exists():
            raise FileNotFoundError(f"Missing local file: {local_file_path}")

        upload_file_to_s3(local_file_path, s3_key)


if __name__ == "__main__":
    upload_raw_files()
