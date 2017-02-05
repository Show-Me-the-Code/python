#!/usr/bin/env python
#coding: utf-8
import redis
import string, random

HOST =  'localhost'
PORT = 6379

#激活码中的字符和数字
field = string.letters + string.digits

#获得四个字母和数字的随机组合
def getRandom():
    return "".join(random.sample(field,4))

#生成的每个激活码中有几组
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

#生成n组激活码
def generate(n):
    return [concatenate(4) for i in range(n)]

#连接到数据库
r = redis.Redis(HOST,PORT)
#生成200组激活码
codelist = generate(200)
#将生成的激活码存入数据库中
for i in xrange(200):
    r.sadd("code",codelist[i])
r.save()

