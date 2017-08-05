'''
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

# encoding: utf-8
import collections
import os

with open('test.txt','r') as fp:
    str1=fp.read().split(' ')
b = collections.Counter(str1)
with open('result.txt','w') as result_file:
    for key,value in b.items():
        result_file.write(key+':'+str(value)+'\n')