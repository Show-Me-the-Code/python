# -*- coding: utf-8 -*- 
import uuid
import redis 

def gen( num):
    assert isinstance(num, int) == True
    assert num > 0
    rst = []
    while True:
        temp = str(uuid.uuid1()).replace('-', '')
        if temp not in rst:
            rst.append(temp)
            num = num - 1
            if num == 0:
                break
    return rst

rst = gen(200)

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

prefix = 'active'

for i in rst:
    r.set('%s_%s' % (prefix, i), i)
    print i

show = r.keys('*')

for i in show:
    print r.get(i)
