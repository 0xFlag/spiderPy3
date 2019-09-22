#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import os
from bs4 import BeautifulSoup

url = "http://www.mzitu.com"

Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding': 'gzip',
    'Referer': 'https://www.mzitu.com/203873'
}
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding': 'gzip',
    'Referer': 'https://www.mzitu.com/203873'
}

html = requests.get(url, headers=Hostreferer)
soup = BeautifulSoup(html.text, "lxml")
pic_max = soup.find_all('a', class_='page-numbers')[3].text

path = os.getcwd() + "/mzitu"

if (os.path.exists(path)):
    pass
else:
    os.makedirs(path)

print('开始执行下载功能')
for i in range(1, int(pic_max) + 1):
    href = url + '/page/' + str(i)
    html = requests.get(href, headers=Hostreferer)
    soup = BeautifulSoup(html.text, "lxml")
    images = soup.find("ul",{"id":"pins"}).find("li").find("span")
    for img in images:
        href1=img['href']
        print(href1)
        response = requests.get(href1, headers=Hostreferer)
        soup = BeautifulSoup(response.text, 'lxml')
        pic_address= soup.find("div",{"class":"main-image"}).find("img")['src']
        pic_name = soup.find("div",{"class":"main-image"}).find("img")['alt']
        print(pic_address)
        content = requests.get(pic_address, headers=Picreferer).content
        # file_name = path + "/" + pic_address[-9:]
        file_name = path + "/" + pic_name + ".jpg"
        with open(file_name, 'wb') as f:
            f.write(content)

print('完成')