#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-12 22:58:23
# @Last Modified by:   30987
# @Last Modified time: 2015-01-12 23:09:12

#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

def word_count(file_path):
	file = open(file_path,'r')
	num = 0
	file.read()
	for line in file:
		line_list = line.split()
		#print line_list
		num += len(line_list)
	file.close()
	return num

if __name__ == '__main__':
	try:
		print 'The total number of words is :',word_count('test.txt')
	except Exception, e:
		print "Can't open file!"