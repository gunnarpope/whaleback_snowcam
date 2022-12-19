"""
  file: upload2s3.py
  Author: Gunnar Pope
  Email:  gunnar@bitstory.ai
  Date:   2022-12-18
  Brief: 
  Usage: 
"""


if __name__ == "__main__":
    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')
    
    filename = 'snowcam/fig/whaleback_snowcam.jpg'
    bucket_name = 'whaleback.snowcam'
    object_name = 'fig/whaleback_snowcam.jpg' 
    
    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filename, bucket_name, filename)

