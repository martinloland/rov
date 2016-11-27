''' 
userInput.py
- Read input from keyboard and USB-controller
- Initiate functions to make the change
'''

def getUserInput():
	buttons = []
	
	if joystickConnected:
		buttons = getJoystick(buttons)
	
	# Toggle keys
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			buttons.append('quit')
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				buttons.append('return')
			# close
			if event.key == pygame.K_ESCAPE:
				buttons.append('quit')
			# LED
			if event.key == pygame.K_l:
				buttons.append('led')
			# info
			if event.key == pygame.K_i:
				buttons.append('info')
			# info
			if event.key == pygame.K_p:
				buttons.append('motorin')
			# overlay
			if event.key == pygame.K_o:
				buttons.append('overlay')
			# reset gimbal
			if event.key == pygame.K_q:
				buttons.append('resetGimbal')
			# snapshot
			if event.key == pygame.K_SPACE:
				buttons.append('snapshot')
			# snapshot
			if event.key == pygame.K_j:
				buttons.append('joystick')
					
	# Gimbal		
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		buttons.append('gLeft')
	if keys[pygame.K_d]:
		buttons.append('gRight')
	if keys[pygame.K_s]:
		buttons.append('gUp')
	if keys[pygame.K_w]:
		buttons.append('gDown')
	if keys[pygame.K_q]:
		buttons.append('gReset')
		
	# Motors
	if keys[pygame.K_UP]:
		buttons.append('mForward')
	if keys[pygame.K_DOWN]:
		buttons.append('mBack')
	if keys[pygame.K_LEFT]:
		buttons.append('mLeft')
	if keys[pygame.K_RIGHT]:
		buttons.append('mRight')
	if keys[pygame.K_z]:
		buttons.append('mDecrease')
	if keys[pygame.K_c]:
		buttons.append('mIncrease')
	if keys[pygame.K_r]:
		buttons.append('mUp')
	if keys[pygame.K_f]:
		buttons.append('mDown')
		
	actOnInput(buttons)
	
def getJoystick(buttons):
	global lastout
	'''
	0:L left/right
	1:up/down
	2: R left/right
	3: up/down 
	4: 1 increase
	5: 2 motors
	6: 3 decrease
	7: 4 overlay
	8: L1 snapshot
	9: R1 up
	11: R2 down
	12: select info
	13: start exit
	14: L3resetGimbal
	15: R3 led
	'''
	out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	it = 0 #iterator
	# Read axis
	for i in range(0, j.get_numaxes()):
		out[it] = j.get_axis(i)
		it+=1
	#Read input from buttons
	for i in range(0, j.get_numbuttons()):
		out[it] = j.get_button(i)
		it+=1
	
	# HOLD KEYS
	# gimbal
	if out[0]>0.8:
		buttons.append('gRight')
	if out[0]<-0.8:
		buttons.append('gLeft')
	if out[1]>0.8:
		buttons.append('gUp')
	if out[1]<-0.8:
		buttons.append('gDown')
		
	#motor
	if out[2]>0.8:
		buttons.append('mRight')
	if out[2]<-0.8:
		buttons.append('mLeft')
	if out[3]>0.8:
		buttons.append('mBack')
	if out[3]<-0.8:
		buttons.append('mForward')
	if out[4]:
		buttons.append('mIncrease')
	if out[6]:
		buttons.append('mDecrease')
	if out[9]:
		buttons.append('mUp')
	if out[11]:
		buttons.append('mDown')
	
		
	# TOGGLE KEYS
	if out[12] and out[12] != lastout[12]:
		buttons.append('info')
	if out[13] and out[13] != lastout[13]:
		buttons.append('quit')
	if out[14] and out[14] != lastout[14]:
		buttons.append('resetGimbal')
	if out[15] and out[15] != lastout[15]:
		buttons.append('led')
	if out[5] and out[5] != lastout[5]:
		buttons.append('motorin')
	if out[7] and out[7] != lastout[7]:
		buttons.append('overlay')
	if out[8] and out[8] != lastout[8]:
		buttons.append('snapshot')

	lastout = out
	
	return buttons

def actOnInput(buttons):
	if any("return" in s for s in buttons):
		toggle_fullscreen()
	if any("quit" in s for s in buttons):
		closeProgram()
	if any("snapshot" in s for s in buttons):
		snapshot()
	if any("overlay" in s for s in buttons):
		if ui.overlay:
			ui.overlay = False
		elif not ui.overlay:
			ui.overlay = True
	if any("motorin" in s for s in buttons):
		if ui.motorInfo:
			ui.motorInfo = False
		elif not ui.motorInfo:
			ui.motorInfo = True
	if any("info" in s for s in buttons):
		if ui.info:
			ui.info = False
		elif not ui.info:
			ui.info = True
	if any("led" in s for s in buttons):
		if act.led:
			act.led = 0
		elif not act.led:
			act.led = 1
	if any("joystick" in s for s in buttons):
		if ui.joystick:
			ui.joystick = False
		elif not ui.joystick:
			ui.joystick = True
	
	gimbal(buttons)
	motor(buttons)