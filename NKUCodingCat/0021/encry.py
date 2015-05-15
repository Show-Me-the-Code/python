#coding=utf-8
import os,time,random,hashlib,math
def md5(str):
	m = hashlib.md5()   
	m.update(str)
	return m.hexdigest()
def Salt(len=64):
	return "%s"*len%tuple([chr(65+random.randint(0,25)) for i in range(len)])
def encry(Str):
	Log = int(math.log(len(Str),2))+1
	MaxLen = 2**Log
	SAL = Salt(MaxLen-len(Str)+random.randint(8,16))
	ENC = md5(Str+SAL)
	return SAL,ENC
print encry("sudgds")