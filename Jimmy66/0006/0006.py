#!/bin/env python
# -*- coding: utf-8 -*- 

import re

#返回英文单词列表
def list1(string):
	words = re.findall(r'[a-zA-Z]+\b',string) #修改了正则表达式
	return words

#从文件中读取数据
def file_read(filename):
	with open(filename,'r') as fp:
		article = fp.read()
		return article

#计算出出现最多的单词
def most_word_number(word_list):
    str_dict = {}
    for item in word_list:
        if item in str_dict:
            str_dict[item] +=1
        else:
            str_dict[item] =1

    str_dict = {str_dict[key]:key for key in str_dict}
    return (max(str_dict),str_dict[max(str_dict)])


if __name__ == '__main__':
	string = file_read('GitHub.txt')
	words = list1(string)
	print (most_word_number(words))
	