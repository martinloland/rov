''' 
ui.py
- Create and update the user interface
'''

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (60,60,60)
GRAYtrans = (60,60,60,150)
STROKE = 2
BIGSTROKE = 7
t=l=0
c=1
b=r=2

class UI:
	def __init__(self):
		self.nbCirclesR = 0
		self.nbCirclesL = 0
		self.overlay = True
		self.info = False
		self.motorInfo = False
		self.joystick = False
		
	def splash(self):
		self.splashImg = pygame.image.load(os.path.join('img', 'splash.jpg'))
		surface.blit(self.splashImg,(0,0))
		pygame.display.flip()
		
	def create(self):
		ui.splash()
		self.circDia = int(surface.get_height()*0.8/4)
		self.circSpace = int(surface.get_height()*0.2/5)
		#Elements
		self.infoScreen = Info()
		self.motors = Motors()
		self.video = Video(0.5, 0.5, c, c)
		self.RollPitch = RollPitch(0.5, 0.5, c, c)
		#Circles
		#self.pitch = Circle(r, 'Pitch', -90, 90, None)
		#self.roll = Circle(r, 'Roll', -90, 90, None)
		self.yaw = Circle(r, 'Yaw', 0, 360, None)
		self.volt = Circle(r, 'Volt', 0, 13.0, 'v')
		#self.curr = Circle(r, 'Curr', 0, 20, 'A')
		self.temp= Circle(r, 'Temp', 4, 30, 'C')
		self.depth= Circle(r, 'Depth', 0, 10, 'm')
		self.led= Circle(l, 'Led', 0, 1, None)
		self.pan= Circle(l, 'Pan', 0, 180, None)
		self.tilt= Circle(l, 'Tilt', 0, 180, None)
		self.pwr= Circle(l, 'Power', 0, 190, None)
	
	def update(self):
		surface.fill(BLACK)
		self.video.draw()
		if self.info:
			self.infoScreen.draw()
		
		else:
			if self.motorInfo:
				self.motors.draw()
			
			if self.overlay:
				self.RollPitch.draw()
				#Circles
				#self.pitch.draw(sens.pitch)
				#self.roll.draw(sens.roll)
				self.yaw.draw(sens.yaw)
				self.volt.draw(sens.volt)
				#self.curr.draw(sens.curr)
				self.temp.draw(sens.temp)
				self.depth.draw(sens.depth)
				self.led.draw(act.led)
				self.pan.draw(act.pan)
				self.tilt.draw(act.tilt)		
				self.pwr.draw(act.pwr)		
		
		pygame.display.flip()
		
class Info:
	def __init__(self):
		self.room = 20
		self.width = surface.get_width() - 2*self.room
		self.height = surface.get_height() - 2*self.room
	
	def draw(self):
		self.face = pygame.Surface((self.width,self.height), pygame.SRCALPHA, 32)
		self.face = self.face.convert_alpha()
		self.face.fill(GRAYtrans)
		if ui.joystick:
			self.keyboard = pygame.image.load(os.path.join('img', 'controller.png'))
		else:
			self.keyboard = pygame.image.load(os.path.join('img', 'keyboard.png'))
		self.keyboardy = self.height - self.room - self.keyboard.get_height()
		self.face.blit(self.keyboard,(self.room,self.keyboardy))
		
		surface.blit(self.face,(self.room,self.room))
		
class Motors:
	def __init__(self):
		self.bg = pygame.image.load(os.path.join('img', 'motors.png'))
		self.width = self.bg.get_width()
		self.height = self.bg.get_height()
		self.x = ui.circSpace*2 + ui.circDia
		self.y = surface.get_height()-ui.circSpace-self.height
		self.xStart = [61, 45, 132, 220, 204]
		self.yStart = [29, 127, 184, 127, 29]
	
	def draw(self):
		self.face = pygame.Surface((self.width,self.height), pygame.SRCALPHA, 32)
		self.face.blit(self.bg,(0,0))
		
		#text
		value = [act.lf, act.lb, act.cb, act.rb, act.rf]
		self.font = pygame.font.Font(None, 30)
		
		for i in range(0,len(value)):
			self.printValue = "%.0f" % value[i]
			self.text = self.font.render(self.printValue, 1, WHITE)
			self.textw = self.text.get_rect()[2]
			self.face.blit(self.text,(self.xStart[i]-self.textw /2,self.yStart[i]+4))
		
		surface.blit(self.face,(self.x,self.y))	

class Circle:
	def __init__(self, side, att, min, max, unit):
	
		if side == r:
			self.nb = ui.nbCirclesR
			self.xstart = surface.get_width()-ui.circSpace-ui.circDia
			ui.nbCirclesR += 1
		elif side == l:
			self.nb = ui.nbCirclesL
			self.xstart = ui.circSpace
			ui.nbCirclesL += 1
		if unit:
			self.unit = unit
		else:
			self.unit = ''
		self.att = att
		self.max = max
		self.min = min
		self.dia = ui.circDia
		self.rad = int(self.dia/2)
		self.ystart = ui.circSpace+(ui.circSpace+ui.circDia)*self.nb
		
	def draw(self, value):
		self.face = pygame.Surface((self.dia,self.dia), pygame.SRCALPHA, 32)
		self.face = self.face.convert_alpha()
		self.rect = self.face.get_rect()
		# Semi transparent circle
		pygame.draw.circle(self.face, GRAYtrans, (self.rad,self.rad), self.rad, 0)
		# Stroke circles
		self.percent = (float(value)-self.min)/(self.max-self.min)
		self.start = math.pi/2
		self.end = math.pi/2+2*math.pi*self.percent		
		pygame.draw.arc(self.face, GRAY, self.rect, 0, 8, BIGSTROKE)
		pygame.draw.arc(self.face, WHITE, self.rect, self.start, self.end, BIGSTROKE)
		# Attribute text
		self.attFont = pygame.font.Font(None, 30)
		self.attText = self.attFont.render(self.att, 1, WHITE)
		self.attTextw = self.attText.get_rect()[2]
		self.face.blit(self.attText,((self.dia-self.attTextw)/2,self.dia*0.27))
		# Value
		self.valueFont = pygame.font.Font(None, 50)
		self.printValue = "%.2f" % value + self.unit #Round to two decimal places
		self.valueText = self.valueFont.render(self.printValue, 1, WHITE)
		self.valueTextw = self.valueText.get_rect()[2]
		self.face.blit(self.valueText,((self.dia-self.valueTextw)/2,self.dia*0.47))	

		surface.blit(self.face,(self.xstart,self.ystart))

class Video:
	def __init__(self, i, j, horJust, verJust):
		self.img = None
		
	def draw(self):		
		surface.blit(pygame.transform.rotate(self.img, 180),(0,0))

class RollPitch:
	def __init__(self, i, j, horJust, verJust):
		# Common
		self.dia = surface.get_height()*0.6
		self.rad = int(self.dia/2)
		self.cor = getXY(i, j, horJust, verJust, self.dia, self.dia)
		# Lines / Pitch
		self.spacing = int(self.rad*0.4)
		self.lines = createLines(self.dia, self.spacing)
		self.lineW = self.lines.get_width()
		self.lineH = self.lines.get_height()
		self.lineCorx = int((self.dia-self.lineW)/2)
		self.lineCory = int((self.dia-self.lineH)/2)
		
	def draw(self):
		self.face = pygame.Surface((self.dia,self.dia), pygame.SRCALPHA, 32)
		self.face = self.face.convert_alpha()
		self.rect = self.face.get_rect()
		#Circle / Roll
		pygame.draw.arc(self.face, GRAY, self.rect, 0, 8, STROKE+1)
		pygame.draw.arc(self.face, WHITE, self.rect, math.pi, math.pi*2, STROKE+1)
	
		offset = sens.pitch/10*self.spacing
		self.face.blit(self.lines,(self.lineCorx,self.lineCory+offset))
		surface.blit(rot_center(self.face,sens.roll),(self.cor[0],self.cor[1]))
			
def createLines(diameter, spacing):
	lineWidth = int(diameter*0.8)
	lines = 17
	height = spacing*(lines-1)
	bg = pygame.Surface((lineWidth,height), pygame.SRCALPHA, 32)
	bg = bg.convert_alpha()
	
	y=0
	for line in range(0,lines):
		if line == (lines-1)/2:
			x = 0
		else:
			x = int(lineWidth*0.35)
		pygame.draw.line(bg, WHITE, (x,y),(lineWidth-x,y),STROKE)
		y = y + spacing
	return bg

def createSurface():
	pygame.init()
	[SCREEN_WIDTH, SCREEN_HEIGHT] = [1296,730]
	surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	pygame.display.set_caption('ROV UI')
	return surface