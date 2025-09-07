import sys
import boto3
from botocore.config import Config
import logging
from aws_automation_labs.config_loader import load_config
from s3_tools import s3io


def main():
    logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    default_config = load_config()  # loads config found in config/default.yaml
    region = default_config["region"]
    bucket = default_config["bucket"]
    s3_config = Config(
            retries={
                "max_attempts": 10,
                "mode": "standard"
            }
        )
    s3 = boto3.client('s3', region_name=region, config=s3_config)
    logger.info("Start S3 Workflow")
    run_s3_flow(s3_client=s3, bucket=bucket)

def run_s3_flow(s3_client, bucket):
    
    s3_key= s3io.upload_to_s3(s3_client, bucket)
    file_size = None
    if s3_key is not None:
        file_size = s3io.verify_upload_to_s3(s3_client, bucket, s3_key)
    else:
        logging.info("File upload failed, stopping execution")
        sys.exit(1)
    if file_size is not None:
        s3io.download_from_s3(s3_client, bucket, s3_key, file_size)

if __name__ == "__main__":
    main()
