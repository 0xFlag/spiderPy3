import requests
from bs4 import BeautifulSoup
import re
import sys

# 忽略警告代码
requests.packages.urllib3.disable_warnings()

def GetRealUrl(url,n):
    try:
        headers1 = {
        'Host': 'v.kuaishou.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'did=web_1714d878938048829e040ac47bce556e; didv=1592886609000; clientid=3; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1592906286,1592921393; sid=441fae0035af15547d45fa4d; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1592921406',
        'Upgrade-Insecure-Requests': '1',
        }

        headers2 = {
        'Host': 'c.kuaishou.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'did=web_1714d878938048829e040ac47bce556e; didv=1592886609000; clientid=3; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1592906286,1592921393; sid=441fae0035af15547d45fa4d; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1592921406',
        'Upgrade-Insecure-Requests': '1',
        }

        response = requests.get(url, headers=headers1, timeout=5, allow_redirects=False,verify=False)
        share_url = response.headers['Location']
        #print(share_url)

        share_response = requests.get(share_url,headers=headers2, timeout=5, verify=False).text
        #print(share_response)

        # 通过BeautifulSoup提取所有script标签里内容
        soup = BeautifulSoup(share_response,'lxml')
        noWaterMarkVideo = soup.select('script[type="text/javascript"]')
        #print(noWaterMarkVideo)

        # 获取第三个script标签里内容
        t = list(noWaterMarkVideo)[3].text
        #print(t)

        # 正则处理字符串获取真实地址
        pattern = re.compile('\"srcNoMark\":"(.*?)"},',re.S)
        real_url = re.findall(pattern,t)[0]

        if n == 2:
            print(real_url)
        elif n == 1:
            print(real_url)
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