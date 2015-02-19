#!/bin/env python
# -*- coding: utf-8 -*- 

#完成了一部分，还没有找出空行和注释行数

import os
import glob

def get_file_list():
	return glob.glob('*')

def file_read(filename):
	with open(filename,'r') as fp:
		linelist = fp.readlines()
		return len(linelist)

if __name__ == '__main__':
	n1 = 0
	os.chdir('./code')
	file_list = get_file_list()
	for name in file_list:
		n1 += file_read(name)
	print '文件夹中的文件总行数为' + str(n1) + '行'
