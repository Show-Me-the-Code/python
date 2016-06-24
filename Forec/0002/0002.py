# coding = utf-8
__author__ = 'Forec'

# 保随机码至MySQL

import pymysql
import random

def make_number( num, length ):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    dic = set()
    i = 0
    while i < num:
        str = ''
        for j in range(length):
            str += random.choice(letters)
        if str not in dic:
            dic |= {str}
            i += 1
        else:
            continue
    return dic

def save( dic ):
    connect = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = 'VKDARK'
    )
    cur = connect.cursor()
    try:
        __create = 'create database if not exists test'
        cur.execute(__create)
    except:
        print('database create error')
    connect.select_db('test')
    __create_table = 'create table if not exists codes(code char(64))'
    cur.execute(__create_table)
    cur.executemany('insert into codes values(%s)',dic)
    
    connect.commit()
    cur.close()
    connect.close()
    
save(make_number(200,10))