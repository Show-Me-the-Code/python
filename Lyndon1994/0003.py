# -*- coding: utf-8 -*-
# **第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis
import random
import string

forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        yield Re


def save_code():
    r = redis.Redis(host='127.0.0.1', port='6379', password='linyii')
    codes = generate_code(200, 20)
    p = r.pipeline()
    for code in codes:
        p.sadd('code', code)
    p.execute()
    return r.scard('code')


if __name__ == '__main__':
    save_code()
