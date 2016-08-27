# -*- coding:utf8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
用于登录lvye.com
'''
url = "https://www.amazon.cn/s/ref=sa_menu_digita_l3_siphone?ie=UTF8&page=1&rh=n%3A665002051%2Cp_89%3AApple%2Cn%3A664978051"

headers = {
   'Host': 'www.amazon.cn',
   'Connection': 'keep-alive',
   'Cache-Control': 'max-age=0',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   'DNT': '1',
   'Referer': 'https://www.amazon.cn/ref=z_cn?tag=zcn0e-23',
   'Accept-Encoding': 'gzip, deflate, sdch, br',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',

}


resp = requests.get(url, headers=headers, allow_redirects=False)

if resp.status_code == 200:
    print 'response headers is:'
    print resp.headers
    with open('amazon.html','wb') as f:
        f.write(resp.text)
