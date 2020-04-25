import re
s=open("s.txt","rb").read()
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') # 匹配模式
url = re.findall(pattern,s.decode('utf-8'))

lines_seen=set()
for line in url:
	if line not in lines_seen:
		lines_seen.add(line)
		with open("u.txt", 'a+') as f:
			f.write(line+'\n')
		f.close()