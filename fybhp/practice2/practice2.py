# -*- coding:utf-8 -*-
import MySQLdb
import MySQLdb.cursors
import string
import random

# 表在workbench中已建好.sql语句见pra2.sql
# 该方法较为底层了，有时间再用SQLAlchemy来实现此脚本.
map = {}
db = MySQLdb.connect(host='localhost',user='root',passwd='501826')
curs = db.cursor()
db.select_db('activation_code')

def id_generator(size=4, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    set = []
    for i in range(4):
        a = ''.join(random.choice(chars) for _ in range(size))
        set.append(a)
    return set

for i in range(200):
    id = '-'.join(id_generator())
    while id in map.values():
        id = '-'.join(id_generator())
    map[i] = id
    curs.execute('insert into mygeneratecode values(%d,%r)'%(i,map[i]))

db.commit()
curs.close()
db.close()