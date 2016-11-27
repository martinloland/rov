''' 
pi.py
- Main program on raspberry pi
- Initiate three processes that run independently
'''

import serial, io, socket, struct, time, picamera, os
import cPickle as pickle
from multiprocessing import Process
execfile(os.path.join('pi', 'proc.py'))
execfile(os.path.join('pi', 'func.py'))
execfile('common.py')

if __name__ == "__main__":
	# local: '10.0.0.111'
	# direct: '169.254.195.12'
	s1 = SOCKET('10.0.0.111', 8000, 'wb')
	s2 = SOCKET('10.0.0.111', 9000, 'wb')
	s3 = socket.socket()
	s3.connect(('10.0.0.111', 9500))

	ser0 = createSerial('/dev/ttyUSB0')
	print('Connected to : ' + ser0.name)
	ser1 = createSerial('/dev/ttyUSB1')
	print('Connected to : ' + ser1.name)
	
	# Find out which arduino is doing what
	waiting = 1	
	while waiting:
		if ser0.readline():
			waiting = 0
			print('Sensor arduino at: ' + ser0.name)
			sensorSerial = ser0
			actuatorSerial = ser1
		elif ser1.readline():
			waiting = 0
			print('Sensor arduino at: ' + ser1.name)
			sensorSerial = ser1
			actuatorSerial = ser0
	
	try:
		
		# Read camera
		p1 = Process(target=readCamera, args=(s1.file,))
		
		# From arduino
		p2 = Process(target=readSerial, args=(sensorSerial,s2.file,))
		
		# To arduino
		p3 = Process(target=sendSerial, args=(actuatorSerial,s3,))
		
		p1.start()
		p2.start()
		p3.start()		
	
	finally:
		s1.close()
		s2.close()
		ser0.close()
		ser1.close()
		print '\n\n * DID SHUTDOWN *\n'