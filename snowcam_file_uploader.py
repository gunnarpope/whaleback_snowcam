"""
  file: snowcam_file_uploader.py
  Author: Gunnar Pope
  Email:  gunnar@bitstory.ai
  Date:   2022-12-18
  Brief: 
  Usage: 
"""


if __name__ == "__main__":
    import boto3
    import logging
    from time import sleep

    # Create an S3 client
    s3 = boto3.client('s3')
    
    filename = 'src/fig/whaleback_snowcam.jpg'
    bucket_name = 'whaleback.snowcam'
    object_name = 'fig/whaleback_snowcam.jpg' 
    
    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    while(True):

        filename = 'src/fig/whaleback_snowcam.jpg'
        s3.upload_file(filename, bucket_name, object_name)
        logging.info('Success pushing snowcam file to s3 bucket.')

        sleep(10)


