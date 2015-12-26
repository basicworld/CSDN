# -*- coding:utf8 -*-
import requests

'''
用于登录lvye.com
'''
url = "http://www.lvye.org/user.php"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
	(KHTML, like Gecko)	 Chrome/47.0.2526.106 Safari/537.36",
	"Content-Type": "application/x-www-form-urlencoded",
	"Host": "www.lvye.org",
	"Content-Length": "39",
}

post_data = {
	"uname": "<your username>",
	"pass": "<your password>",
	"op": "login",
}

resp = requests.post(url, headers=headers, data=post_data, allow_redirects=False)

if resp.status_code == 200:
	print 'response headers is:'
	print resp.headers
	if 'Set-Cookie' in resp.headers:
		print 'login success!!'
