#!/usr/bin/python3

import requests
import time
from bs4 import BeautifulSoup

referer = {
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
	'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	'Accept-Encoding': 'gzip',
	'Referer': 'https://passport2.chaoxing.com'
}

def spider(href):
	try:
		html = requests.get(href, headers=referer)
		soup = BeautifulSoup(html.text, "lxml")
		schoolname = soup.find('span', id="schoolName2").get_text().strip()
		sschoolname = href + "\n" + schoolname + "\n"
		print(sschoolname)
		write(sschoolname)
	except Exception as e:
		pass
	#continue

def write(sschoolname):
	with open("schoolname.txt", 'a+') as f:
		f.write(sschoolname)

if __name__ == "__main__":
	for i in range(1, 33333):
		url = "https://passport2.chaoxing.com/login?fid="
		href = url + str(i)
		spider(href)