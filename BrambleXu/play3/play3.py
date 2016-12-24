# -*- coding:utf-8 -*-
#**第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。
'''
running successfully

here are some useful links:
https://www.tutorialspoint.com/redis/redis_keys.htm
http://redis.io/topics/data-types-intro

But I found there is no table in redis, even if I stored the code in the redis database,
if I use SET 1 haha(1 is the key, haha is the value), then the original value(the code) will be replace by haha
how to avoid this?
I think I should read more code to find the answer
'''

import redis

def store_redis(filepath):
    r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
    f = open(filepath, 'rb')
    i = 0
    for line in f.readlines():
        code = line.strip()
        r.set(i, code)
        i += 1



if __name__ == '__main__':
    store_redis('Running_result.txt')
