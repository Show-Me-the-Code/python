#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        create_a_table_and_put_keys.py
# Create Date: 2015-02-09 12:12:43
# Usage:       create_a_table_and_put_keys.py 
# Descripton:  create a table in mysql and put keys into it

"""
第 0002 题：
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""

from uuid import uuid4
import MySQLdb as mdb


def generate_key(num):
    key_list = [str(uuid4()) for i in range(num)]
    return key_list


def create_a_table_and_put_keys(key_list):
    with mdb.connect('localhost', 'test', '123', 'testdb') as cur:
        
        # create table
        cur.execute("DROP TABLE IF EXISTS rkeys")
        cur.execute("CREATE TABLE rkeys(\
                      key_value CHAR(40) NOT NULL\
                      )")

        # insert data
        # I want to use executemany, but there is a library bug...
        # It seems that executemany cannot match single-string list
        # cur.executemany("INSERT INTO rkeys VALUES(%s)", key_list)
        for i in key_list:
            cur.execute("INSERT INTO rkeys(key_value)\
                         VALUES('%s')" % i)


def main():
    create_a_table_and_put_keys(generate_key(200))


if __name__ == '__main__':
    main()
