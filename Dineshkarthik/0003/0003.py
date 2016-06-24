#!/usr/local/bin/python
#coding=utf-8
__author__ = 'Dineshkarthik'

#0003 Title: The 0001 title generated 200 activation code (or coupon) to save Redis non-relational databases.

from walrus import *

def redis_store(count):
    db=Database(host='localhost',port=6379,db=0)
    h = db.List("activation_code")
    for i in range(count):
        s = str(uuid.uuid4().get_hex().lower()[0:8])
        h.extend([s])

if __name__ == '__main__':
    redis_store(200)