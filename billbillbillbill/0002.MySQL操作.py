#!/usr/bin/env python
#coding: utf-8
import MySQLdb
import string, random


#激活码中的字符和数字
field = string.letters + string.digits

#获得四个字母和数字的随机组合
def getRandom():
    return "".join(random.sample(field,4))

#生成的每个激活码中有几组
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

#生成n组激活码
def generate(n):
    return [concatenate(4) for i in range(n)]



HOST =  'localhost'
USER = 'root'
PASSWORD = '000ooo'
PORT = 3306
DB = 'python'
#连接数据库
conn = MySQLdb.connect(
    host =HOST,
    user=USER,
    passwd=PASSWORD,
    db=DB,
    port=PORT)
cur = conn.cursor()

#生成200组激活码
codelist = generate(200)
#将生成的激活码插入到表中
for i in xrange(200):
    sql = 'INSERT INTO code (code) VALUES (\'%s\')' % codelist[i]
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()
