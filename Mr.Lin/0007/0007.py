#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-14 11:07:02
# @Last Modified by:   30987
# @Last Modified time: 2015-01-14 11:47:11
#第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
#
#

"""
此处统计的注释行#  并不会将#!/usr/bin/env python # -*- coding: utf-8 -*- 统计在内，同时if __main__里面的注释也不会进行统计


def code_count(code_file):
	total_lines = 0
	empty_lines = 0
	comment_lines = 0

	file_object = open(code_file,'r')
	for line in file_object:
		word_list = line.split()
		#print word_list
		if word_list == []:
			empty_lines += 1
		elif word_list[0] == '#':
			comment_lines += 1
		total_lines += 1

	file_object.close()
	#print("Total line: %s. Empty lines :%s.Comment lines:%s"% (total_lines,empty_lines,comment_lines))
	return total_lines,empty_lines,comment_lines


if __name__ == '__main__':
	t,e,c=code_count('0007.py')
	print("Total line: %s. Empty lines :%s.Comment lines:%s"%(t,e,c))


