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
        html.encoding = 'utf-8'
        return html.text
    except Exception as e:
            print(e)
 
def get_url(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    a = []
    tx = soup.find_all('div', class_='txList')
    for href in tx:
        a.append('https://www.woyaogexing.com' + str(href.a['href']))
        title = str(href.a['title'])
        print(title)
        for url in a:
            blogger_html = get_html(url)
            soup = BeautifulSoup(blogger_html, 'lxml')
            img = soup.find_all(name='li', class_='tx-img')
            for image_link in img:
                image_url = 'https:' + image_link.a['href']
                download(image_url)

def download(image_url):
    ref = requests.get(image_url)
    img = ref.content
    #path = os.getcwd() + "/download/"
    filename = "./download/" + image_url.split('/')[-1]
    print('download: {}'.format(image_url))
    with open(filename, 'wb') as file:
        file.write(img)

if __name__ == '__main__':
    #url ='https://www.woyaogexing.com/touxiang/z/ktecy/index.html'
    page = range(2,4)
    for i in page:
        print(i)
        url = 'https://www.woyaogexing.com/touxiang/z/ktecy/index_{}.html'.format(i)
        get_url(url)