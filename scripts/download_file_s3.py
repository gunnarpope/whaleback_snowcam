"""
  file: download_file_s3.py
  Author: Gunnar Pope
  Email:  gunnar@bitstory.ai
  Date:   2022-12-18
  Brief: 
  Usage: 
"""


if __name__ == "__main__":
    import boto3
    import botocore
    
    BUCKET_NAME = 'whaleback.snowcam' # replace with your bucket name
    KEY = 'fig/whaleback_snowcam.jpg' # replace with your object key
    
    s3 = boto3.resource('s3')
    
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
