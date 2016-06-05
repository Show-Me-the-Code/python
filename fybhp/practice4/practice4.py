# -*- coding:utf-8 -*-
import redis

db = redis.Redis(host = 'localhost',port = 6379,db = 0)
file = open('./English.txt','r')
s = set()
map = {}
allLines = file.readlines()
for eachLine in allLines:
    alist = eachLine.split()
    if alist != []:
        for i in alist:
            if i[-1] == '.':
                i = i[:-1]
            if i == '':
                continue
            i = i.lower()
            if not i in s:
                db.set(i,1)
                s.add(i)
            else:
                db.incr(i)
    else:
        pass
print s
for i in s:
    map[i] = db.get(i)
print map