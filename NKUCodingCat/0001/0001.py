#coding=utf-8
import os,time,random,hashlib
def md5(str):
	m = hashlib.md5()   
	m.update(str)
	return m.hexdigest()
def salt():
	return "%s"*5%tuple([random.randint(10000000,99999999) for i in range(5)])
res = [md5(salt()+str(time.time())) for i in range(200)]
path = os.path.split(os.path.realpath(__file__))[0]+"/"
f = open(path+"code.txt","w")
for i in res:
	f.write(i+"\n")
f.close()