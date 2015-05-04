#coding=utf-8
#其实以前写过这样的东西来着= =……
import re,sys,os
path = os.path.split(os.path.realpath(__file__))[0]
Fliter = re.compile("[^A-Za-z-\']|((?<![A-Za-z])[-\'])|([-\'](?![A-Za-z]))")
Divider = re.compile("\s")
File = open(path+"\\input.txt").read()
Data =  Divider.split(Fliter.sub(" ",File))
Dict = {}
for i in Data:
	j = i.lower()
	try:
		Dict[j]+=1
	except KeyError:
		Dict[j] =1
	except:
		raise 
for i in  Dict.items():
	print "%s:%s"%i
