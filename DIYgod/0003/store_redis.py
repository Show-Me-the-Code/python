# -*- coding: utf-8 -*-

import redis

def store_redis(filepath):
    r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
    f = open(filepath, 'rb')
    for line in f.readlines():
        code = line.strip()
        r.lpush('code', code)

if __name__ == '__main__':
    store_redis('Activation_code.txt')
