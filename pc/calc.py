''' 
calc.py
- Convert strings to/from classes
- Calculate placement for UI elements
'''

# Motor directions
# Change to "-1" to reverse
r_lf = -1
r_rf = -1
r_lb = 1
r_cb = 1
r_rb = 1

def classToString(act):
	#str = 'ACT,led:1,pan:120,tilt:43,lf:0,rf:0,lb:100,rb:110'
	string = ('ACT' + 
			',led:' + str(act.led) +
			',pan:' + str(act.pan) +
			',tilt:' + str(act.tilt) +
			',lf:' + str(act.lf*r_lf) +
			',rf:' + str(act.rf*r_rf) +
			',lb:' + str(act.lb*r_lb) +
			',cb:' + str(act.cb*r_cb) +
			',rb:' + str(act.rb*r_rb))
	return string
	
def stringToClass(string):
	if string.find('SENSORS') != -1:
		list = string.split(',')
		
		# Write to class
		for index in list:
			seperator = index.find(':')
			if seperator > 0:
				name = index[0:seperator]
				number = float(index[seperator+1:len(index)])
				setattr(sens, name, number)
				
		#Calculate and set depth
		setattr(sens, 'depth', (sens.press-1.0)*10.0)
		
		#Fix pitch if overflow
		if sens.pitch > 180:
			sens.pitch = 0
	
def sendString(string, connection):
	actuator.update(string)
	pickle.dump(actuator, connection, pickle.HIGHEST_PROTOCOL)			
	connection.flush()

def getXY(i, j, horJust, verJust, width, height):
	#Returns x and y value for position of image on screen
	cor = []
	faceWidth = surface.get_width()
	faceHeight = surface.get_height()
	cor.append(None)
	# X
	if horJust == l:
		cor[0] = int(faceWidth*i)
	elif horJust == c:
		cor[0] = int(faceWidth*i-width/2)
	elif horJust == r:
		cor[0] = int(faceWidth*i-width)
	#y
	cor.append(None)
	if verJust == t:
		cor[1] = int(faceHeight*j)
	elif verJust == c:
		cor[1] = int(faceHeight*j-height/2)
	elif verJust == b:
		cor[1] = int(faceHeight*j-height)	
	return cor

def rot_center(image, angle):
    #rotate an image while keeping its center and size
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image