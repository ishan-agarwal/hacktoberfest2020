from socket import *

s = socket(AF_INET, SOCK_STREAM)

port = 444

s.bind(('', port))

s.listen(5)
print("The socket is listening")

while True : 
	c, addr = s.accept()
	sentence = c.recv(1024)

	cap_sen = sentence.upper()
	c.send(cap_sen)

	c.close()