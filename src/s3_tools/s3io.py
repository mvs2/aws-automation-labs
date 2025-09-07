"""
Upload, list, and download files from an S3 bucket.
Also verify file size of downloaded file is the same as the file size uploaded to the S3 bucket.
Makes use of config/default.yaml for region/bucket config.
"""
from botocore.config import Config
import logging
logger = logging.getLogger(__name__)
from botocore.exceptions import ClientError
from aws_automation_labs.config_loader import load_config
from pathlib import Path


def upload_to_s3(s3_client, bucket_name):
    fixture_path = Path(__file__).resolve().parents[2] / "data" / "fixtures" / "test_textdata.txt"
    file_name = fixture_path.name
    s3_key = f"incoming/{file_name}"
    try:
        s3_client.upload_file(str(fixture_path), bucket_name, s3_key)
        logger.info(f"Uploaded {s3_key} to {bucket_name}")
        return s3_key
    except ClientError as e:
        logger.error(f"Failed to upload {s3_key} to {bucket_name}: {e}", exc_info=True)
        return None

def verify_upload_to_s3(s3_client, bucket_name, file_to_verify):
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=file_to_verify)
        logger.info(f"Verified {file_to_verify}: size={response['ContentLength']} bytes, last modified={response['LastModified']}")
        return response["ContentLength"]
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == "404" or error_code == "NoSuchKey" or error_code == "NotFound":
            logger.error(f"File {file_to_verify} not found.", exc_info=True)
            return None
        elif error_code == "403":
            logger.error(f"Access denied for file {file_to_verify} in bucket {bucket_name}.", exc_info=True)
            return None
        else:
            logger.error(f"Unexpected error occurred: {e}", exc_info=True)
            return None


def download_from_s3(s3_client, bucket_name, s3_key, orig_size):
    logger.info(f"Downloading {s3_key} from {bucket_name}")
    dl_path = Path(__file__).resolve().parents[2] / "data" / "downloads" / f"{Path(s3_key).name}"
    try:
        s3_client.download_file(bucket_name, s3_key, dl_path)
        # size verification compared to original
        dl_size = Path(dl_path).stat().st_size
        logger.info(f"Downloaded file size is {dl_size} in bytes and original size is {orig_size} in bytes.")
        if dl_size == orig_size:
            logger.info("File sizes match")
        else:
            logger.warning("CAUTION: File sizes do not match")
    except ClientError as e:
        logger.error(f"Failed to download {s3_key} to {bucket_name}: {e}", exc_info=True)


