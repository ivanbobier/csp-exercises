 import socket
# AF_INET refers address from the internet, it requires pair of a host and port number
# SOCK_STREAM is use to create TCP protocol
s = socket.socket(socket.AF_INET,, socket.SOCK_STREAM)
# gethostname is use when client and server is on the same computer or device
s.bind(socket.gethostname(), 1025)
s.listen(5)
 
 while True:
 	
 		clt, adr = s.accept()
 		print(f"Connection to {adr} established")
 		clt.send(bytes("Socket Programming in Python", "utf-8"))
 # clt.Close closes the connection
 		clt.close()