echo 'Images sent to  "http://localhost:8081/snowcam"'
echo 'Image Files sent to fig/whaleback_snowcam.jpg'
echo 'Streaming snowcam pictures....'
motion -c snowcam/motion.cfg -l log/motion.log 
