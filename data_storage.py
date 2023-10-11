import json
import boto3


class S3:
    def __init__(self, aws_access_key, aws_secret_key, bucket_name):
        self.s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        self.bucket_name = bucket_name

    def upload_file(self, local_path, s3_key):
        self.s3.upload_file(local_path, self.bucket_name, s3_key)
        print(f"Uploaded {local_path} to {s3_key}")
        

    def download_file(self, s3_key, local_file):
        local_path=f"{'/Users/gouravdeepsingh/Desktop'}/{local_file}"
        self.s3.download_file(self.bucket_name, s3_key, local_path)
        print(f"Downloaded {s3_key} to {local_path}")
        

        



        
        