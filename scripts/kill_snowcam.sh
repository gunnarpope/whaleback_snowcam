# find the pid of the motion program
ps -ef ¦ grep motion

# send a kill command to the pid you found earlier.
# kill -s SIGHUP <pid>
