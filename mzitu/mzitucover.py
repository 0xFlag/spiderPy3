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
soup = BeautifulSoup(html.text, "html.parser")
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
    soup = BeautifulSoup(html.text, "html.parser")
    images = soup.find_all('img', class_='lazy')

    for img in images:
        file_name = img['data-original']
        print(file_name)
        content = requests.get(file_name, headers=Picreferer).content
        file_name = path + "/" + file_name[-20:]
        with open(file_name, 'wb') as f:
            f.write(content)

print('完成')