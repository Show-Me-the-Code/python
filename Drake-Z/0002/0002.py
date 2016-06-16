#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。'

__author__ = 'Drake-Z'

import mysql.connector

def write_to_mysql(filename):
    f = open(filename, 'r')
    conn = mysql.connector.connect(user='root', password='******', database='test')
    print('登录数据库成功')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS user")
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    print('创建表成功')
    a = 1
    for line in f.readlines():
        line = line[:-1]                     #直接除去最后一个字符的所有字符，这里去除\n符号
        cursor.execute('insert into user (id, name) values (%s, %s)', [str(a), line])
        conn.commit()
        a += 1
    cursor.close()
    print('插入数据结束')
    return 0

def search_mysql():
    b = input('查询第几号（1-200）激活码：')
    conn = mysql.connector.connect(user='root', password='******', database='test')
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', (b,))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()
    return 0

if __name__ == '__main__':
    filename = 'active_code.txt'
    write_to_mysql(filename)
    search_mysql()