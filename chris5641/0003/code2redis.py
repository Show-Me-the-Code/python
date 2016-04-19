# -*- coding: utf-8 -*-
"""
第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""
import redis
__author__ = 'Chris5641'


def code2redis():
    i = 0
    f = open('ActivationCode.txt', 'r')
    r = redis.Redis(host='localhost', port=6379)
    for line in f.readlines():
        r.zadd('codes', line.strip(), i)
        i += 1


if __name__ == '__main__':
    code2redis()
