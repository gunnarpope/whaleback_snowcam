#!/bin/bash
# run.sh
# Start image collection for the snowcam and push results to s3 bucket
echo 'Images sent to  "http://localhost:8081/snowcam"'
echo 'Image Files sent to fig/whaleback_snowcam.jpg'
echo 'Use scripts/kill_snowcam.sh to find and remove the running motion program.'
echo 'Streaming snowcam pictures....'
motion -c src/motion.conf -l log/motion.log &

echo 'Running uploader to s3 bucket every 5 seconds...'
# python3 snowcam_file_uploader.py
