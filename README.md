#NTNU ROV

Open source ROV project by students at IPM NTNU for Trondheim Makers and high school students. Group 1.

##Contributors
 - Written by Martin Løland
 - MPU6050 library by Jeff Rowberg
 
##Features
 - Live streaming of video from raspberry pi / piCamera to computer over socket communcation
 - Aprox 15fps with 0.4 ms latency at 1296x730 resolution
 - Two ways communication of data to/from arduino/rpi and computer using serial communication and pickle with sockets
 - Custom made GUI using pygame with support for keyboard and USB-controller input

##Arduino
 - Reading sensors and moving actuators (motors, led etc.)
 - Sending and receiving values to/from raspberry pi
 
##Raspberry pi
 - Reading images from picamera
 - Sending camera and sensor feed to computer
 - Forwarding actuator settings from computer to arduino
 
##Computer
 - Program to receive sensor and camera feed
 - Displaying UI with updated data
 - Taking user input and changing actuators accordingly

#Installation
Tekst her

## Raspberry Pi
 - Tested on rpi 2 and 3
 - Assuming fresh installation of raspbian and basic knowledge of rpi/linux
 - "sudo raspi-config" -> expand filesystem, enable camera, enable ssh
 - Update and upgrade -> https://www.raspberrypi.org/documentation/raspbian/updating.md
 - Install pip -> "sudo apt-get install python-pip"
 - Install picamera -> "sudo apt-get install python-picamera" & "sudo pip install picamera"
 - Install serial -> "python -m pip install pyserial"
 - If no errors during this process the rpi should be able to run the code
 
 ## Computer
 - Tested on windows 10
 - Install python 2.7.X -> https://www.python.org/downloads/
 - Install pygame -> http://pygame.org/
