
# Enable the motion package and stream to http://localhost:8081/
```
$ sudo motion

```

# Website
[motion](https://motion-project.github.io/motion_config.html#configfiles)

# Dev Notes
1. Copy the default `motion.conf` file into your working directory.
1. Run `sudo motion` to start the webcam
1. View the result on `http://localhost:8081/`
1. Disable the localhost-only viewing setting.

# Installation
1. motion
1. ssh


# Design Considerations  
1. Security (run a non-root)
  1. Port forwarding
  1. Remote Proxy
  1. Reverse proxy for viewing at scale
  1. Static IP configuration
1. SSH login for remote repairs
1. Logging
  1. Motion logs
  1. Root logs
  1. Access logs

## SSH login for remote repairs
```
$ sudo systemctl enable ssh
$ sudo systemctl start ssh
``` 

# Find your hostname
```
pi@raspberrypi:~/Desktop/whaleback_snowcam/motion $ hostname
raspberrypi
```

## Find your IP address
```
pi@raspberrypi:~/Desktop/whaleback_snowcam/motion $ ip a | grep inet
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host 
    inet 192.168.1.151/24 brd 192.168.1.255 scope global dynamic noprefixroute wlan0
    inet6 fe80::eca5:e090:f625:2ade/64 scope link 
```

## Connect remotely to RPi
```
$ ssh pi@[raspberrypi_ip_address]
```

## Create a new user to run the motion application as non-root user
```
$ sudo adduser gunnar
```
## Login as a different user
```
$ gunnar@snowcam:~ $ su - gunnar
Password: 
gunnar@snowcam:~ $
gunnar@snowcam:~ $ ls
gunnar@snowcam:~ $ 
```  

The new user does't belong to any groups. Add the user to a group so they can see the whaleback_snowcam files and run the motion script.

## Make sure the user doesn't have root access
```
gunnar@snowcam:~ $ sudo -l

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for gunnar: 
Sorry, user gunnar may not run sudo on snowcam.

```

# Create a new usergroup to share the whaleback_snowcam/ folder between pi (root) user and gunnar
[tutorial](https://www.tecmint.com/create-a-shared-directory-in-linux/)
```
pi@snowcam:~/Desktop $ sudo groupadd snowcam
pi@snowcam:~/Desktop $ sudo usermod -a -G snowcam gunnar
pi@snowcam:~/Desktop $ sudo chgrp -R snowcam whaleback_snowcam/
pi@snowcam:~/Desktop $ sudo chmod -R 2775 whaleback_snowcam/
pi@snowcam:~/Desktop $ 
```


# Disable sleep mode
xset -dpms

# Simultaneous connections
Only 6 simulteneous connections to localhost:8081 can be made that stream photos.


