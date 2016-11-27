''' 
func.py
- Communication for socket and serial
'''

class SOCKET:
	def __init__(self, ip, port, direction):
		self.conn = socket.socket()
		self.conn.connect((ip, port))
		self.file = self.conn.makefile(direction)
		
	def close(self):
		self.file.close()
		self.conn.close()

def createSerial(port):
	ser = serial.Serial(
		port = port,
		baudrate = 115200,
		timeout = 1
	)
	ser.close()
	ser.open()
	return ser