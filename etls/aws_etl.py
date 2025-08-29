import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY, AWS_REGION

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon=False,
            key=AWS_ACCESS_KEY_ID,
            secret=AWS_ACCESS_KEY,
            client_kwargs={"region_name": AWS_REGION}
        )
        print("Connected to S3")
        return s3
    except Exception as e:
        print("Error connecting to S3: {e}")
        raise

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket: str):
    try:
        bucket_uri = f"s3://{bucket}"
        if not s3.exists(bucket_uri):
            s3.mkdir(bucket_uri)
            print("Bucket created")
        else:
            print("Bucket already exists")
    except Exception as e:
        print(f"Failed to create bucket: {e}")
        raise

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, s3_file_name: str):
    try:
        s3.put(file_path, f"s3://{bucket}/raw/{s3_file_name}")
        print("File uploaded to S3")
    except Exception as e:
        print(f"Failed to upload: {e}")
        raise
