#!bin/env python 
# -*- coding: utf-8 -*-

#导入模块，进行正则匹配
import re

#计算单词个数
def counter(string):
	words = re.findall(r'[a-zA-Z]+(\'[a-zA-Z]+|\b)',string) #修改了正则表达式
	amount = len(words)
	return str(amount)

#从文件中读取数据
def file_read(filename):
	with open(filename,'r') as fp:
		article = fp.read()
		return article

#主函数
if __name__ == '__main__':
	string = file_read('GitHub.txt')
	result = counter(string)
	print  'There are', result, 'words in this article.'
	print  '这篇文章中有' + result + '个英文单词'

	
			