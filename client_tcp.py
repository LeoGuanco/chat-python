import socket
import sys
import threading

class cliente(object):
	"""Clase del cliente para un chat simple"""
	def __init__(self, host='localhost', port=10000):
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.connect((host,port))

		#hilo para poder escuchar lo que manda el servidor
		listen = threading.Thread(target = self.listen_msg)
		listen.demon = True		
		listen.start()

		# bucle con la condicion de fin para el servidor
		self.message = ''
		try:
			while self.message != 'salir':
				self.message = input('> ')
				if self.message != '':
					try:
						self.sock.send(self.message)
					except e:
						print('error al enviar el mensaje')
						print(e)
			self.sock.close()		
		except:
			self.sock.close()

	def listen_msg(self):
		while True:
			try:
				msg = self.sock.recv(1024)
				print(msg)
			except Exception as e:
				print('error al recibir mensaje')
				print(e)


client = cliente()