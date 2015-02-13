#coding=utf-8
#并没有redis所以我只是抄官网的示例代码
import os,re,redis
path = os.path.split(os.path.realpath(__file__))[0]+"/"
f = open(path+"code.txt","r")
A = f.read()
arr = re.split("\s+",A)
r = redis.Redis(host='localhost', port=6379, db=0)
for i in range(len(arr)):
	if i:
		r.set(str(i),arr[i])
r.save()