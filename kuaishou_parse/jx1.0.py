import requests
from bs4 import BeautifulSoup
import re
import sys

# 忽略警告代码
requests.packages.urllib3.disable_warnings()

ua_phone = 'Mozilla/5.0 (Linux; Android 6.0; ' \
'Nexus 5 Build/MRA58N) AppleWebKit/537.36 (' \
'KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36'

def GetRealUrl(url,n):
	try:
		headers = {
		'User-Agent': ua_phone,
		'Content-Type': 'application/x-www-form-urlencoded',
		'Referer': 'https://kphbeijing.m.chenzhongtech.com',
		}

		response = requests.get(url, headers=headers, timeout=5, allow_redirects=False,verify=False)
		share_url = response.headers['Location']
		#print(share_url)

		share_response = requests.get(share_url,headers=headers, timeout=5, verify=False).text
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