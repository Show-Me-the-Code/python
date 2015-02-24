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
            str_dict[item] += 1
        else:
            str_dict[item] = 1
#非常漂亮的写法，来自于别人的代码，下面那个是我看到这个后自己写的，但是这个有一个比较奇怪的问题，在sublime中少打一行或者略作修改，保存的结果会不同，我也解释不清楚为什么            
    str_dict = {str_dict[key]:key for key in str_dict}
    return (max(str_dict),str_dict[max(str_dict)])
#   temp = {}
#   for key in str_dict:
#   	temp[str_dict[key]] = key
#   return max(temp),temp[max(temp)]



if __name__ == '__main__':
	string = file_read('GitHub.txt')
	words = list1(string)
	times,word = most_word_number(words)
	print '出现最多的单词为' + str(word) + '，出现了' + str(times) + '次'
	