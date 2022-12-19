"""
  file: upload2s3.py
  BITSTORY.AI LLC ("COMPANY") CONFIDENTIAL
  Copyright (C) 2022 BITSTORY.AI LLC, All Rights Reserved.
  
  NOTICE:  All information contained herein is, and remains the property of COMPANY. The intellectual and technical concepts contained
  herein are proprietary to COMPANY and may be covered by U.S. and Foreign Patents, patents in process, and are protected by trade secret or copyright law.
  Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained
  from COMPANY.  Access to the source code contained herein is hereby forbidden to anyone except current COMPANY employees, managers or contractors who have executed 
  Confidentiality and Non-disclosure agreements explicitly covering such access.
  
  The copyright notice above does not evidence any actual or intended publication or disclosure  of  this source code, which includes  
  information that is confidential and/or proprietary, and is a trade secret, of  COMPANY.   ANY REPRODUCTION, MODIFICATION, DISTRIBUTION, PUBLIC  PERFORMANCE, 
  OR PUBLIC DISPLAY OF OR THROUGH USE  OF THIS  SOURCE CODE  WITHOUT  THE EXPRESS WRITTEN CONSENT OF COMPANY IS STRICTLY PROHIBITED, AND IN VIOLATION OF APPLICABLE 
  LAWS AND INTERNATIONAL TREATIES.  THE RECEIPT OR POSSESSION OF  THIS SOURCE CODE AND/OR RELATED INFORMATION DOES NOT CONVEY OR IMPLY ANY RIGHTS  
  TO REPRODUCE, DISCLOSE OR DISTRIBUTE ITS CONTENTS, OR TO MANUFACTURE, USE, OR SELL ANYTHING THAT IT  MAY DESCRIBE, IN WHOLE OR IN PART.

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

