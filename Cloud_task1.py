import boto3
import os
from datetime import datetime

# Output file to log result
with open("output.txt", "w") as log:

    bucket_name = "codtech-intern-umar-bucket123"  # must be unique globally
    region = "us-east-1"

    s3 = boto3.client("s3", region_name=region)

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": region}
        )
        log.write(f"[{datetime.now()}] Bucket '{bucket_name}' created.\n")
    except Exception as e:
        log.write(f"[{datetime.now()}] Bucket creation error: {str(e)}\n")

    folder = "uploaded_files"
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        try:
            s3.upload_file(path, bucket_name, filename, ExtraArgs={'ACL': 'public-read'})
            log.write(f"[{datetime.now()}] Uploaded {filename} successfully.\n")
        except Exception as e:
            log.write(f"[{datetime.now()}] Upload error for {filename}: {str(e)}\n")
