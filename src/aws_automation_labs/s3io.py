import boto3
from botocore.exceptions import ClientError

from aws_automation_labs.config_loader import load_config
from pathlib import Path

config = load_config() #loads config found in config/default.yaml
region = config["region"]
bucket = config["bucket"]
fixture_path =Path(__file__).resolve().parents[2] /"data" / "fixtures" / "planets.csv"
file_name = fixture_path.name
s3_key = f"incoming/{file_name}"
s3 = boto3.client('s3', region_name=region)
try:
    s3.upload_file(str(fixture_path), bucket, s3_key)
    print(f"Uploaded {s3_key} to {bucket}")
except ClientError as e:
    print(f"Failed to upload {s3_key} to {bucket}: {e}")

