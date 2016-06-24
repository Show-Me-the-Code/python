# coding = utf-8
__author__= 'liez'

import random
import sqlite3

def make_number(num, length):
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    a = []
    i = 0
    while i < num:
        numstr = ''
        for j in range(length):
            numstr += random.choice(str)
        if numstr not in a: #如果没重复
            a.append(numstr)
            i += 1
    print(a)
    return a

def save(a):
    try:
        connect = sqlite3.connect('codelist.db')
    except:
        print("failed")
    cur = connect.cursor()
    cur.execute('create table if not exists codes(code char(20) primary key)')
    for item in a:
        cur.execute('insert into codes values (?)', [item])
    print("success")
    connect.commit()
    cur.close()
    connect.close()

save(make_number(20, 10))
