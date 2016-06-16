#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。'

__author__ = 'Drake-Z'

import redis

def write_to_redis(filename):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.flushdb()
    f = open(filename, 'r').readlines()
    for line, num in zip(f, range(1, len(f)+1)):
        line = line[:-1]                     #去除\n符号
        r.set(num, line)
    return 0

def search_redis():
    b = int(input('Search Active code（1-200）：'))
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    print(str(r.get(b),'UTF-8'))
    return 0

if __name__ == '__main__':
    filename = 'active_code.txt'
    write_to_redis(filename)
    search_redis()