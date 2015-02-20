#!/bin/env python
# -*- coding: utf-8 -*- 

#算是完成了，查找Python中的#开头的单行注释足够了，不过计算/**/的单行乃至多行注释还没有做到，也暂时不想写。
#在字符串（全文读入）或者字符串（分段读取）组成的list中计算出行数长度或者摘录出想要的部分内容是我下一步要思考的问题
#目前掌握的正则在单行情况下还比较理想，多行就比较吃力了，顺便想多自己写一些，不是不想用库，是有的库给出的方式不是我想要的，比如解析XML对于作为纯用户的直观感较差

import os
import glob
import re

def get_file_list():
	return glob.glob('*')

def file_read(filename):
	n2 = n3 = 0 
	with open(filename,'r') as fp:
		linelist = fp.readlines()
	for string in linelist:
		if re.match(r'#', string) != None:
			n2 += 1
		elif re.match(r'^ *\n', string) != None:
			n3 += 1
	return len(linelist),n2,n3

if __name__ == '__main__':
	n1 = n2 = n3 = 0
	os.chdir('./code')
	file_list = get_file_list()
	for name in file_list:
		n1 += file_read(name)[0]
		n2 += file_read(name)[1]
		n3 += file_read(name)[2]
	print '文件夹中的文件总行数为' + str(n1) + '行'
	print '文件夹中的注释总行数为' + str(n2) + '行'
	print '文件夹中的空行总行数为' + str(n3) + '行'
	print '文件夹中的代码总行数为' + str(n1-n2-n3) + '行'