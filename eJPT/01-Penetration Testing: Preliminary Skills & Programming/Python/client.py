import socket
import sys


if __name__ == '__main__':
	HOST=bytes(sys.argv[1],"utf-8")
	PORT=int(sys.argv[2])

	client=socket.socket()

	client.connect((HOST,PORT))
	client.sendall(b"Hello From The Client Side!!")

	print(client.recv(1024))

	client.close()