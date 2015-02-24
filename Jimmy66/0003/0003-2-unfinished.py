#!bin/env python 
# -*- coding: utf-8 -*-

#这是另一种方案

#未完成，想法是直接将返回的字典存入redis数据库，感觉这样都是键值对，看上去舒服点，性能上会怎么样，不清楚
#还需要补习面向对象方面的python知识，文档还不能完全看懂

from redisco import models  

def file_read(filename):
	with open(filename,'r') as f:
		lines = f.readlines()
	for n in range(0,200):
		lines[n] = lines[n].strip()
	num = range(1,201)
	d = dict(zip(num,lines))
	print d

def redis_write(dictionary):




if __name__ == '__main__':
	file_read('result.txt')