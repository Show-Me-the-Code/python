# -*- coding:utf-8 -*-

file = open('./English.txt','r')
s = set()
map = {}
allLines = file.readlines()

def pre(i):
    if not i in s:
        map[i] = 1
        s.add(i)
    else:
        map[i] += 1

for eachLine in allLines:
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
                        pre(j)
                    continue
                pre(i)
        else:
            pass
print s
print map