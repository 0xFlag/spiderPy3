import shutil
readPath='ks1.txt'
writePath='ook.txt'
lines_seen=set()
outfiile=open(writePath,'a+',encoding='utf-8')
f=open(readPath,'r',encoding='utf-8')
for line in f:
	if line not in lines_seen:
		outfiile.write(line)
		lines_seen.add(line)