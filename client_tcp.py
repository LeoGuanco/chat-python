import socket
import sys
import threading

class Cliente(object):
	"""Clase del cliente para un chat simple"""
	def __init__(self, host='localhost', port=10000):
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.connect((host,port))

		#hilo para poder escuchar lo que manda el servidor
		listen = threading.Thread(target = self.listen_msg)
		listen.daemon = True		
		listen.start()

		# bucle con la condicion de fin para el servidor
		self.message = ''
		try:
			while self.message != 'salir':				
				if self.message != '':
					try:
						self.sock.send(self.message.encode('utf-8'))
					except:
						pass
				self.message = input('> ')
			self.sock.close()		
			sys.exit()
		except:
			self.sock.close()
			sys.exit()

	def listen_msg(self):
		while True:
			try:
				msg = self.sock.recv(1024)
				print(msg)
			except:
				pass


client = Cliente()