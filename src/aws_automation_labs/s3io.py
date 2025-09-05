'''
Upload, list, and download files from an S3 bucket.
Also verify file size of downloaded file is the same as the file size uploaded to the S3 bucket.
Makes use of config/default.yaml for region/bucket config.
'''
import boto3
from botocore.exceptions import ClientError
from aws_automation_labs.config_loader import load_config
from pathlib import Path


def main():
    config = load_config()  # loads config found in config/default.yaml
    region = config["region"]
    bucket = config["bucket"]
    s3 = boto3.client('s3', region_name=region)
    file = upload_to_s3(s3, bucket)
    file_size = verify_upload_to_s3(s3, bucket, file)
    if file_size is not None:
        download_from_s3(s3, bucket, file, file_size)

def upload_to_s3(s3_client, bucket_name):
    fixture_path = Path(__file__).resolve().parents[2] / "data" / "fixtures" / "planets.csv"
    file_name = fixture_path.name
    print(f"file_name in upload is {file_name}")
    s3_key = f"incoming/{file_name}"
    try:
        s3_client.upload_file(str(fixture_path), bucket_name, s3_key)
        print(f"Uploaded {s3_key} to {bucket_name}")
    except ClientError as e:
        print(f"Failed to upload {s3_key} to {bucket_name}: {e}")
    return s3_key

def verify_upload_to_s3(s3_client, bucket_name, file_to_verify):
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=file_to_verify)
        print(f"Verified {file_to_verify}: size={response['ContentLength']} bytes, last modified={response['LastModified']}")
        return response["ContentLength"]
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == "404":
            print(f"File {file_to_verify} not found.")
            return None
        elif error_code == "403":
            print(f"Access denied for file {file_to_verify} in bucket {bucket_name}.")
            return None

def download_from_s3(s3_client, bucket_name, s3_key, orig_size):
    print(f"Downloading {s3_key} from {bucket_name}")
    dl_path = Path(__file__).resolve().parents[2] / "data" / "downloads" / f"{Path(s3_key).name}"
    try:
        s3_client.download_file(bucket_name, s3_key, dl_path)
        # size verification compared to original
        dl_size = Path(dl_path).stat().st_size
        print(f"Downloaded file size is {dl_size} in bytes and original size is {orig_size} in bytes.")
        if dl_size == orig_size:
            print("File sizes match")
        else:
            print("CAUTION: File sizes do not match")
    except ClientError as e:
        print(f"Failed to download {s3_key} to {bucket_name}: {e}")


if __name__ == '__main__':
    main()








