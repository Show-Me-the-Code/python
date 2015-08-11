# coding=utf-8
#**第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

import redis

def read_line(file):
	f = open(file,'r')
	lines = f.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].strip()
	return lines

def redis_save():
	lines = read_line('random_key.out')
	r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0)

	for i in range(len(lines)):
		key = str(i+1)
		value = str(lines[i])
		r.set(key, value)
		print 'ok'
	r.save()
	for i in range(len(lines)):
		print r.get(i)
	print 'OK!'

if __name__ == '__main__':
	redis_save()