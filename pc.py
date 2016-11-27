#!/usr/bin/env python
''' 
win.py
- read data from raspberry pi
- read user input from keyboard and USB-controller
- create user interface
- send signal to raspberry pi
'''

import socket, pygame, sys, time, math, os, StringIO, datetime
import cPickle as pickle
from pygame import gfxdraw
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
execfile(os.path.join('pc', 'calc.py'))
execfile(os.path.join('pc', 'ui.py'))
execfile(os.path.join('pc', 'func.py'))
execfile(os.path.join('pc', 'userInput.py'))
execfile('common.py')

fullscreen = False
uiTest = True #True when just testing the UI, no comm

surface = createSurface() # Pygame main surface
ui = UI() # Initatie UI
ui.create() # Create UI
sens = SENS() #Sensor class
act = ACT() #Actuator class

# Joystick
joystickConnected = pygame.joystick.get_count()
if joystickConnected:
	j = pygame.joystick.Joystick(0)
	j.init()
	lastout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Pickle classes
img = dataIMG() 
sensor = dataSENS()
actuator = dataACT()

if not uiTest:
	#Sockets
	camSock = SOCKET('0.0.0.0',8000)
	senSock = SOCKET('0.0.0.0',9000)
	actSock = SOCKET('0.0.0.0',9500)
	actFile = actSock.conn.makefile('wb')

while True:
	if not uiTest:
		try:
			# CAMERA
			f = camSock.conn.makefile('rb')
			img = pickle.load(f)
			f.close()
			imgbuf = StringIO.StringIO(img.img)
			ui.video.img = pygame.image.load(imgbuf)
			# SENSOR
			f = senSock.conn.makefile('rb')
			sensor = pickle.load(f)
			f.close()
			stringToClass(sensor.sensordata)
		except:
			None		
	else:
		data = 'SENSORS,press:2.12457,temp:18.30,volt:10.23,curr:2.24,roll:15,yaw:0,pitch:10,ax:0,ay:0,az:0,compass:13.5'
		stringToClass(data)	
		ui.video.img = pygame.image.load(os.path.join('img', 'videoH.jpg'))
	
	# Update screen
	ui.update()
	
	#Get user input
	getUserInput()
	
	if not uiTest:
		#Generate string and send it
		strToSend = classToString(act)
		actuator.actuatordata = strToSend	
		pickle.dump(actuator, actFile, pickle.HIGHEST_PROTOCOL)			
		actFile.flush()