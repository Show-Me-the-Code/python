# -*- coding:utf-8 -*-
import os

'''practice5中遍历目录中文件的方法，读取所有文件，
practice4中对单词计数的方法，对所有词进行计数，
完成对map字典的排序即可。'''
diarydir = r'./diary/'
file_list = os.walk(diarydir)
s = set()
map = {}

def pre(i,s):
    if not i in s:
        map[i] = 1
        s.add(i)
    else:
        map[i] += 1

def parselines(allLines):
    for eachLine in allLines:
        #将set置于此处，控制其作用域。
        s = set()
        alist = eachLine.split()
        if alist != []:
            for i in alist:
                i = i.lower()
                if i[-1] == '.' or i[-1] == ',' or i[-1] == "'" or i[-1] == '?' :
                    i = i[:-1]
                    if i == '':
                        continue
                if '.' in i:
                    a = i.split('.')
                    for j in a:
                        pre(j,s)
                    continue
                pre(i,s)
        else:
            pass

for root, dirs, files in file_list:
    for file in files:
        map = {}
        filedir = os.path.join(diarydir,file)
        diary = open(filedir,'r')
        allLines = diary.readlines()
        parselines(allLines)
        #黑科技。
        dict= sorted(map.iteritems(), key=lambda d:d[1], reverse = True)
        print str(file)+'\n'
        print dict
        del map