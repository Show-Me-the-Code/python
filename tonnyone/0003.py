
#coding=utf-8
__author__ = 'tonnytwo'

import redis
import random

r = redis.StrictRedis(host='localhost', port=6379, db=0)
for a in xrange(0,200):
    str1 = ""
    for b in xrange(0,4):
        str1 = str1 + str(random.randint(0,9))
    print str1
    r.set(a, str1)


