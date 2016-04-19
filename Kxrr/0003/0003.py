#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Kxrr'

import redis

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

cache = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

# Store
with open('codeResult.txt', 'r') as f:
    keyList = []
    for lineNum, eachCode in enumerate(f.readlines()):
        keyList.append(lineNum)
        cache.set(str(lineNum), eachCode)

# Read
for i in keyList:
    print cache.get(str(i))


