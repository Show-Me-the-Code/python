#coding=utf-8
#拿以前代码改的
import re,sys,os
path = os.path.split(os.path.realpath(__file__))[0]+"/"
Fliter = re.compile("[^A-Za-z-\']|((?<![A-Za-z])[-\'])|([-\'](?![A-Za-z]))")
Divider = re.compile("\s")
File = open(path+"list.txt").read()
ex = re.split("[\r\n]",File)
ex.append(" ")
ex.append("")
ex = list(set(ex))
def Stat(input):
	Dict = {}
	File = open(input).read()
	Data =  Divider.split(Fliter.sub(" ",File))
	for i in Data:
		j = i.lower()
		try:
			Dict[j]+=1
		except KeyError:
			Dict[j] =1
		except:
			raise 
	
	for i in ex:
		j = i.lower()
		try:
			del(Dict[j])
		except KeyError:
			pass
		except:
			raise
	return  sorted(Dict.items(),key = lambda i:i[1],reverse=True)[0][0]
ls = os.listdir(path+"src/")
for i in ls:
	print i,Stat(path+"src/"+i)