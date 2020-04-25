import sys

def seen():
	lines_seen=set()
	outfiile=open("ks.txt",'a+',encoding='utf-8')
	f=open("ks1.txt",'r',encoding='utf-8')
	for line in f:
		if line not in lines_seen:
			outfiile.write(line)
			lines_seen.add(line)
	f.close()

def write(s):
	with open("ks1.txt", 'a+') as f:
		f.write(s)
	f.close()
	seen()

def sort():
	result=[]
	with open('k.txt','r') as f:
		for line in f:
			result.append(line.strip('\'').split(',')[0])
			result.sort()
			#result=sorted(result)
			s = "".join(result)
		f.close()
		write(s)

if __name__ == '__main__':
	sort()