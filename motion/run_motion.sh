echo 'Motion config file location: /home/pi/Desktop/whaleback_snowcam/motion/motion.conf'
echo 'Images sent to  "http://localhost:8081/snowcam"'
motion -c motion.cfg -l log/motion.log 
# sudo motion -l log/motion.log # don't run as root!
