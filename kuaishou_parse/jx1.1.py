import requests
from bs4 import BeautifulSoup
import re
import sys

# 忽略警告代码
requests.packages.urllib3.disable_warnings()

def GetRealUrl(url,n):
	try:
		headers1 = {
		'Host': 'f.kuaishou.com',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Cookie': 'clientid=3; did=web_694fcd89e07bcb674321c8e8929ea11e; client_key=65890b29; didv=1587783933000',
		'Upgrade-Insecure-Requests': '1',
		}

		headers2 = {
		'Host': 'kphshanghai.m.chenzhongtech.com',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Cookie': 'did=web_9959bc084cfa49fdb680ef01fc3773c0; didv=1587358247000; sid=94933ae1a1785cc77d9691c5',
		'Upgrade-Insecure-Requests': '1',
		}

		response = requests.get(url, headers=headers1, timeout=5, allow_redirects=False,verify=False)
		share_url = response.headers['Location']
		#print(share_url)

		share_response = requests.get(share_url,headers=headers2, timeout=5, verify=False).text
		#print(share_response)

		# 通过BeautifulSoup提取无水印播放地址字符串
		soup = BeautifulSoup(share_response,'lxml')
		noWaterMarkVideo = soup.find(attrs={'id': 'hide-pagedata'}).attrs['data-pagedata']
		#print(noWaterMarkVideo)

		# 正则处理字符串获取真实地址
		pattern = re.compile('\"srcNoMark\":"(.*?)"},',re.S)
		real_url = re.findall(pattern,noWaterMarkVideo)[0]

		if n == 2:
			print(real_url)
		elif n == 1:
			with open("ks.txt", 'a+') as f:
				f.write(real_url+'\n')
				f.close()

	except Exception as e:
		print(e)

if __name__ == '__main__':
	if ".txt" in sys.argv[1]:
		n=1
		with open(sys.argv[1]) as f:
			for line in f.readlines():
				line = line.strip()
				GetRealUrl(line,n)
	else:
		n=2
		link = sys.argv[1]
		GetRealUrl(link,n)