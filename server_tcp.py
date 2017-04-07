import socket
import sys
import threading

class servidor(object):
	"""Servidos basico para chat, hecho en python3 """
	def __init__(self, host='localhost',port=10000):
		self.clients = []

		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.bind((host,port))
		self.sock.listen(5)
		self.sock.setblocking(False)

		# hilos para mandar msj y aceptar las conexiones		
		acept = threading.Thread(target = self.acept_client)
		acept.daemon = True
		acept.start()

		conect = threading.Thread(target = self.recv_msg)
		conect.daemon = True
		conect.start()

		# bucle con la condicion de fin para el servidor		
		try:
			while True:
				message = input('> ')
				if message == 'salir':					
					self.sock.close()	
		except:
			self.sock.close()

	def acept_client(self):
		while True:			
			try:
				client_socket_server, client_address = self.sock.accept()
				client_socket_server.setblocking(False)
				self.clients.append(client_socket_server)
			except Exception as e:
				print(e)
		

	def send_msg_clients(self,msg,client):
		for receiver in self.clients:
			try:
				if receiver != client:
					receiver.send(msg)
			except:
				self.clients.remove(receiver)

	def recv_msg(self):
		while True:
			if len(self.clients) > 0:
				for client_socket in self.clients:
					try:
						msg = client_socket.recv(1024)
						if msg:
							self.send_msg_clients(msg,client_socket)
					except Exception as e:
						print(e)

serv = servidor()