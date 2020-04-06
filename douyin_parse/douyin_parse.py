import os
import sys
import time
import requests
from lxml import etree

ua_phone = 'Mozilla/5.0 (Linux; Android 6.0; ' \
'Nexus 5 Build/MRA58N) AppleWebKit/537.36 (' \
'KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36'

ua_win ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
'AppleWebKit/537.36 (KHTML, like Gecko) ' \
'Chrome/80.0.3987.116 Safari/537.36'

def banner():
	print("Usage: douyin_download.py [Options]")
	print("Options:")
	print("douyin_download.py url")
	print("douyin_download.py *.txt")

def download(path, video_url, file_name):
	if not os.path.exists(path):
		os.mkdir(os.getcwd() + '\\douyin_download')
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':\n' + '正在创建下载文件夹：douyin_download' + '\n\n')
	os.chdir(path)
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':\n' + file_name + '\n开始下载...' + '\n\n')
	r = get_resp_video(video_url)
	with open(file_name, 'wb') as mp4:
		for trunk in r.iter_content(chunk_size=1024 * 1024):
			if trunk:
				mp4.write(trunk)
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':\n' + file_name + '\n下载完成！' + '\n\n')

def get_resp_video(url):
	headers = {
	'User-Agent': ua_phone
	}
	resp = requests.get(url, headers=headers, stream=True)
	return resp

def findUrlInScript(script):
	test = script.split('playAddr: "', 1)
	test = test[1].split('",', 1)
	like_link = test[0]
	link = like_link.replace('playwm', 'play').strip()
	return link

def get_resp(url, ua_win):
	headers = {
	'User-Agent': ua_win
	}
	resp = requests.get(url, headers=headers)
	if resp:
		return resp
	else:
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':\n' + '链接错误' + '\n\n')

def parse_sharelink(link):
	resp = get_resp(link, ua_win)
	re_link = resp.url
	re_resp = get_resp(re_link, ua_win)
	et = etree.HTML(re_resp.text)

	script = et.xpath("/html/body/div/script[3]/text()")[0]
	script = (str(script))
	id = et.xpath("//*[@id='pageletReflowVideo']/div/div[2]/div[2]/div/div[2]/p/text()")[0].split('@')[1]
	content = et.xpath("//*[@id='pageletReflowVideo']/div/div[2]/div[2]/p/text()")[0]
	content = content.split('#')[0].split(',')[0].split('。')[0].split('?')[0].split('？')[0].split('，')[0].split('!')[0].split('！')[0]
	name = id + '：' + content + '.mp4'
	return name, findUrlInScript(script)

def download_click(link):
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':\n' + link + '\n')
	name, _url = parse_sharelink(link)
	resp = get_resp(_url, ua_phone)
	last_url = resp.url
	download('./douyin_download', last_url, name)
	os.chdir('..')

if __name__ == '__main__':
	try:
		if ".txt" in sys.argv[1]:
			with open(sys.argv[1]) as f:
				for line in f.readlines():
					line = line.strip()
					download_click(line)
		else:
			link = sys.argv[1]
			download_click(link)
	except Exception as e:
		banner()