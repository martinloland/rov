''' 
proc.py
- read serial and send to pc
- read camera and send to pc
- get actuator settings from computer and send to rpi
'''

def readSerial(ser, connection):	
	sens = dataSENS()
	while True:
		input = ser.readline().rstrip()
		print input
		sens.update(input)
		pickle.dump(sens, connection, pickle.HIGHEST_PROTOCOL)			
		connection.flush()

def readCamera(connection):		
	img = dataIMG()
	
	with picamera.PiCamera() as camera:
		camera.resolution = (1296, 730)
		#camera.resolution = (640, 480)
		camera.framerate = 24
		# time.sleep(2)
		start = time.time()
		stream = io.BytesIO()
		
		# Use the video-port for captures
		for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):			
			connection.flush()
			stream.seek(0)			
			imgdata = stream.read()			
			img.update(imgdata)
			pickle.dump(img, connection, pickle.HIGHEST_PROTOCOL)
			#print ('Image sent')
			stream.seek(0)
			stream.truncate()

def sendSerial(ser, s):
	actuator = dataACT()
	#output = 'ACT,led:1,pan:120,tilt:43,lf:0,rf:0,lb:100,cb:45,rb:110'
	while True:
		f = s.makefile('rb')
		actuator = pickle.load(f)
		f.close()
		output = actuator.actuatordata.rstrip()
		ser.write(output)
		#time.sleep(0.05)