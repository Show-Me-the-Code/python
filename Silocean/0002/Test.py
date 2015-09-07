# -*-coding:utf-8-*-
__author__ = 'Tracy'

import MySQLdb

conn = MySQLdb.connect('localhost', 'root', '123456', 'test', charset='utf8')
cursor = conn.cursor()

sql = 'create table if not exists mykeys (key_id char(36) not null)'
cursor.execute(sql)

with open('keys.txt', 'r') as f:
    keys = f.readlines()
    for key in keys:
        cursor.execute("insert into mykeys values ('%s')" % str(key))

cursor.close()
conn.commit()
conn.close()