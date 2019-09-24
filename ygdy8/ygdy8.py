#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import os
import re
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
    try:
        html = requests.get(url, headers=headers)
        html.raise_for_status()
        html.encoding = 'gb2312'
        return html.text
    except Exception as e:
            print(e)

def get_star(url):
	html = get_html(url)
	soup = BeautifulSoup(html, 'lxml')
	m = soup.find('a', text=re.compile("末页"))
	n = m['href'].strip()[8:-5]
	page = range(1,int(n)+1)
	for i in page:
		url = 'https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
		print(url)
		get_url(url)
 
def get_url(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    hr = soup.find_all('table', class_='tbspan')
    site = 'https://www.ygdy8.net'
    for rh in hr:
        aa = rh.find('a', text=re.compile("《"))
        td = rh.find('td', text=re.compile("IMD"))
        if td is not None:
            scoreStr = re.findall(r"评分 (.+?)/10", td.text)
            if(len(scoreStr) > 0):
                score = float(scoreStr[0])
                #if(score > 1):
                name = aa.text
                url = site + aa['href']
                #print('url:', url)
                print('title:', name)
                #print('score:', score)
                htm = get_html(url)
                sou = BeautifulSoup(htm, 'lxml')
                h = sou.find('td', attrs={"style": "WORD-WRAP: break-word"})
                downloadA = h.find('a')
                z = downloadA['href']
                #print('down:', z + "\r\n")
                movie = 'url:' + url + '\ntitle:' + name + '\nscore:' + str(score) + '\ndown:' + z + "\r\n"
                get_save(movie)

def get_save(movie):
    with open("ygdy8.txt", 'a+') as f:
        f.write(movie)

if __name__ == '__main__':
	if os.path.exists("ygdy8.txt"):
		os.remove("ygdy8.txt")
		url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
		get_star(url)
	else:
		url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
		get_star(url)