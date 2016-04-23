# coding = utf-8
__author__= 'liez'

import re
def num(path):
    with open(path, 'r') as file:
        data=file.read()
        print(data)
        words=re.compile('[a-zA-Z0-9]+') #compile好像是必须用的，用来格式转换什么的,然后才能进行匹配之类的操作
        dict={}

        for x in words.findall(data):
            if x not in dict:
                dict[x]=1
            else:
                dict[x]+=1

        print(dict)

num('liez.txt')
