#coding:utf8
import sys,os,re

def cal(path):
	filelist = os.listdir(path)
	#print filelist
	filelist = (item for item in filelist if item.endswith('.py'))
	ret = [0,0,0]
	for item in filelist:
		res =  calfile(path,item)
		for i in (0,1,2):
			ret[i] += res[i]	
	return tuple(ret)

def calfile(path,filename):
	totline = 0
	blankline = 0
	commentline = 0
	fileobj = open(path + filename,'r')
	linelist = fileobj.readlines()
	totline = len(linelist)
	for line in linelist:
		pattern = re.compile(r'(\s*)#')
		pattern1 = re.compile(r'(\s*)$')
		if pattern.match(line):
			commentline += 1
		if pattern1.match(line):
			blankline += 1
	fileobj.close()
	return totline,blankline,commentline

#path = r'/home/evan/Desktop/py/python/evan69/0007/'
path = sys.argv[1]
data = cal(path)
dic = dict(zip(['total line','blank line','comment line'],list(data)))
print dic

