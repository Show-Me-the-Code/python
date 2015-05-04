#!bin/env python 
# -*- coding: utf-8 -*-

#导入库
import redis

#打开文件，取出激活码
def file_read(filename):
	with open(filename,'r') as f:
		lines = f.readlines()
	for n in range(0,200):
		lines[n] = lines[n].strip()
	return lines 

#存入数据库
def redis_write():
	lines = file_read('result.txt')
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	for n in range(0,200):
		key = str(n+1)
		value = str(lines[n])
		r.set(key, value)
	r.save()
	print 'finish'

#执行主函数
if __name__ == '__main__':
	redis_write()