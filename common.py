''' 
common.py
- Classes used in Pickle for rpi and windows
'''

class dataIMG:
	def __init__(self):
		self.img = None
	def update(self, image):
		self.img = image

class dataSENS:
	def __init__(self):
		self.sensordata = None
	def update(self, sensor):
		self.sensordata = sensor

class dataACT:
	def __init__(self):
		self.actuatordata = None
	def update(self, actuator):
		self.actuatordata = actuator