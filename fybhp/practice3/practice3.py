# -*- coding:utf-8 -*-
import redis
import string
import random

map = {}
db = redis.Redis(host = 'localhost',port = 6379,db = 0)
p = db.pipeline()

def id_generator(size=4, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    set = []
    for i in range(4):
        a = ''.join(random.choice(chars) for _ in range(size))
        set.append(a)
    return set

for i in range(200):
    id = '-'.join(id_generator())
    while id in map.values():
        id = '-'.join(id_generator())
    map[i] = id
    p.set(i,map[i])

p.execute()
p.save()
#for i in range(200):
    #print str(i) + str(db.get(i))
print db.keys()