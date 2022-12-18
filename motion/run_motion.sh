echo 'Images sent to  "http://localhost:8081/snowcam"'
echo 'Image Files sent to fig/whaleback_snowcam.jpg'
echo 'Streaming snowcam pictures....'
motion -c motion.cfg -l log/motion.log 
# sudo motion -l log/motion.log # don't run as root!
