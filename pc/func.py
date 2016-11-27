''' 
func.py
- General classes
- Handling events initatied by user input
'''

class SENS:
	def __init__(self):
		self.press = 1.0
		self.temp = 0
		self.volt = 0
		self.curr = 0
		self.roll = 0
		self.yaw = 0
		self.pitch = 0
		self.ax = 0
		self.ay = 0
		self.az = 0
		self.compass = 0
		self.depth = 0

class ACT:
	def __init__(self):
		self.led = 0
		self.pan = 90
		self.tilt = 90
		self.lf = 0
		self.rf = 0
		self.lb = 0
		self.cb = 0
		self.rb = 0
		self.pwr = 100

class SOCKET:
	def __init__(self, ip, port):
		self.socket = socket.socket()
		self.socket.bind((ip, port))
		self.socket.listen(5)
		self.conn, self.addr = self.socket.accept()
		
	def close(self):
		None

def closeProgram():
	if not uiTest:
		actFile.close()
	pygame.quit()
	sys.exit()	
	
def snapshot():
	filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()) + '.jpg'
	filename = filename.replace(':','.')
	print filename
	path = os.path.join('snapshots', filename)
	pygame.image.save(pygame.transform.rotate(ui.video.img, 180), path)				
	#Flash
	surface.fill(WHITE)
	pygame.display.flip()

def motor(buttons):
	moving = False
	pwrIncrement = 6
	max = 190
	min = 0
	thresholdU = max-pwrIncrement
	thresholdL = pwrIncrement
	dev = math.sin(math.radians(sens.pitch))
	
	#Power
	if any("mDecrease" in s for s in buttons) and act.pwr >= thresholdL:
		act.pwr -= pwrIncrement
	if any("mIncrease" in s for s in buttons) and act.pwr <= thresholdU:
		act.pwr += pwrIncrement
	
	# Turning
	if any("mForward" in s for s in buttons): #forward
		moving = True
		act.lb = act.pwr
		act.rb = act.pwr
	if any("mBack" in s for s in buttons): #backward
		moving = True
		act.lb = -act.pwr
		act.rb = -act.pwr
	if any("mLeft" in s for s in buttons):
		moving = True
		act.lb = -act.pwr
		act.rb = act.pwr
	if any("mRight" in s for s in buttons):
		moving = True
		act.lb = act.pwr
		act.rb = -act.pwr
	
	#up/down
	if any("mUp" in s for s in buttons):
		moving = True
		act.lf = act.rf = sorted([-max, int(act.pwr*(1-dev)), max])[1]
		act.cb = sorted([-max, int(act.pwr*(1+dev)), max])[1]
	if any("mDown" in s for s in buttons):
		moving = True
		act.lf = act.rf = sorted([-max, int(-act.pwr*(1+dev)), max])[1]
		act.cb = sorted([-max, int(-act.pwr*(1-dev)), max])[1]
		
	if not moving:
		act.lf = act.rf = act.lb = act.cb = act.rb = 0

def toggle_fullscreen():
	global fullscreen
	[SCREEN_WIDTH, SCREEN_HEIGHT] = [1296,730]
	if fullscreen == False:
		pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN)
		fullscreen = True
	else:
		pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		fullscreen = False
	
def gimbal(buttons):
	increment = 6
	panMax = 30
	tiltMax = 55
	zeroPoint = 90
	threshP = [-panMax+increment, panMax-increment]
	threshT = [-tiltMax+increment, tiltMax-increment]
	if any("gRight" in s for s in buttons) and act.pan-zeroPoint > threshP[0]:
		act.pan -= increment
	if any("gLeft" in s for s in buttons) and act.pan-zeroPoint < threshP[1]:
		act.pan += increment
	if any("gDown" in s for s in buttons) and act.tilt-zeroPoint > threshT[0]:
		act.tilt -= increment
	if any("gUp" in s for s in buttons) and act.tilt-zeroPoint < threshT[1]:
		act.tilt += increment
	if any("resetGimbal" in s for s in buttons):
		act.pan = act.tilt = 90