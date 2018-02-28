#--*-- coding:utf-8 --*--
'''
第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
sudo apt-get install redis-server
redis-server
redis-cli
进入命令行
set name gongqingkui

Edit /etc/redis/redis.cnf 
comment the bind 127.0.0.1
'''

from __future__ import print_function
import redis
import random,sys

def activecode(cl):
    codechart='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=[random.choice(codechart) for i in range(cl)]
    return (''.join(s))

def activecodes(cc,cl):
    for cc in range(0,cc):
        s=activecode(cl)
        print(''.join(s))

def getredis():
    r =redis.StrictRedis(host='192.168.1.3',port=6379,db=0)
    return r

def saveactivecode(key,activecode):
    r=getredis()
    r.set(key,activecode)

    
if __name__ =='__main__':
    for i in range(20):
        saveactivecode(i,activecode(32))
