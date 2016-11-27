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
