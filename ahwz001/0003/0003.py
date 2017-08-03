#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0003
* by ahwz001
* 2017/7/22
* thanks this project, I learned some very useful Program.
"""

import redis


def ReadKeys():
    """Read keys form file,and return as a list."""
    res = []
    with open("the_keys_bill.txt") as fobj:
        for line in fobj:
            t = line.strip()
            res.append(t)
    return res


def StoreRedis(keys):
    """save the keys to redis """
    r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
    i = 1
    for key in keys:
        r.set(i, key)
        i += 1
    # print r.keys()
    for i in r.keys():
        print r.get(i)
    r.save()


def main():
    bill = ReadKeys()
    StoreRedis(bill)


if __name__ == '__main__':
    main()