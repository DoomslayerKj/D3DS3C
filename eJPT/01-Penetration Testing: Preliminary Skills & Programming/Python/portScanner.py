import socket
import sys
import pyfiglet
from datetime import datetime
import os

# f=Figlet(font='slant')
# print(f.renderText('SAMPLE TEXT'))
os.system('clear')
banner=pyfiglet.figlet_format("Y2KJ's PORT SCANNER")
print(banner)
if (len(sys.argv) < 2 or len(sys.argv) > 2):
	print(f"Usage: python3 {sys.argv[0]} HOST-IP")
	sys.exit(1)

HOST=bytes(sys.argv[1],"utf-8")

print("*"*50)
print(f"Scanning {HOST}")
print(f"Scanning Started at {str(datetime.now())}")
print("*"*50)

try:
	for port in range(0,65535):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		result=s.connect_ex((HOST,port))
		if result == 0:
			print(f"PORT OPEN: {port}")
		s.close()
except KeyboardInterrupt:
	print("\nExiting..")
	sys.exit()
except socket.gaierror:
	print("Couldn't resolve HOSTNAME!")
	sys.exit()

except socket.error:
	print("Server Not Responding!")
	sys.exit()





