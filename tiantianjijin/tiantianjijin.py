import requests
import random
import re
import json

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]

referer_list = [
    'http://fund.eastmoney.com/110022.html',
    'http://fund.eastmoney.com/110023.html',
    'http://fund.eastmoney.com/110024.html',
    'http://fund.eastmoney.com/110025.html'
]

def ttjijin():
	header = {'User-Agent': random.choice(user_agent_list),
		'Referer': random.choice(referer_list)
	}

	req = requests.get('http://fund.eastmoney.com/js/fundcode_search.js', timeout=5, headers=header)

	fund_code = req.content.decode()
	fund_code = fund_code.replace("﻿var r = [","").replace("];","")
	#print(fund_code)
	
	fund_code = re.findall(r"[\[](.*?)[\]]", fund_code)

	fund_code_list = []
	for sub_data in fund_code:
		data = sub_data.replace("\"","").replace("'","")
		data_list = data.split(",")
		fund_code_list.append(data_list)
	for i in range(len(fund_code_list)):
		#print(fund_code_list[i][0],fund_code_list[i][1],fund_code_list[i][2],fund_code_list[i][3],fund_code_list[i][4])
		
		req = requests.get("http://fundgz.1234567.com.cn/js/" + str(fund_code_list[i][0]) + ".js", timeout=5, headers=header)
		if "jsonpgz" not in req.text or "jsonpgz()" in req.text:
			pass
		else:
			data = (req.content.decode()).replace("jsonpgz(","").replace(");","").replace("'","\"")
			data_dict = json.loads(data)

			fundcode = data_dict['fundcode']
			name = data_dict['name']
			jzrq = data_dict['jzrq']
			dwjz = data_dict['dwjz']
			gsz = data_dict['gsz']
			gszzl = data_dict['gszzl']
			gztime = data_dict['gztime']

			print(fundcode + " | " + name + " | " + jzrq + " | " + dwjz + " | " + gsz + " | " + gszzl + " | " + gztime + "\n")
			
			'''
			with open('./ttjijin.txt', 'a+', encoding='utf-8') as f:
				f.write(fundcode + " | " + name + " | " + jzrq + " | " + dwjz + " | " + gsz + " | " + gszzl + " | " + gztime + "\n")
				f.close()
			'''

if __name__ == '__main__':
	ttjijin()