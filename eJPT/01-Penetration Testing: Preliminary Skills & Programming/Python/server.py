#!/usr/bin/env python3
import socket
import sys
    # socket()
    # bind()
    # listen()
    # accept()
    # connect()
    # connect_ex()
    # send()
    # recv()
    # close()


if __name__ == '__main__':
	
	HOST=bytes(sys.argv[1],"utf-8")
	PORT=int(sys.argv[2])


	#TCP
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
		server.bind((HOST,PORT))
		server.listen(5) #queue of 5
		print(f"Server runninng on {HOST}:{PORT}")
		conn,addr = server.accept()
		print(f"Connection from {addr}!")
		conn.send(bytes("Hello From The Server Side!!","utf-8"))
		data=conn.recv(1024)
		print(f"{data}")
	#UDP 
	#i=0
	# server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	# server.bind((HOST,PORT))
	# print(f"Server runninng on {HOST}:{PORT}")
	
	# while(True):

	# 	data,addr=server.recvfrom(1024)
	# 	print(f"Connection from {addr}!")

	# 	print(f"Data Received: {data}")
	# 	server.sendto(f"Test {i}",(addr,4444))
	# 	i=i+1
	# conn.close()
