# -*- coding: utf-8 -*- 
import uuid
import MySQLdb

def gen( num):
    assert isinstance(num, int) == True
    assert num > 0
    rst = []
    while True:
        temp = str(uuid.uuid1()).replace('-', '')
        if temp not in rst:
            rst.append(temp)
            num = num - 1
            if num == 0:
                break
    return rst

rst = gen(200)
for i in rst:
    print i

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
    cur=conn.cursor()
     
    cur.execute('create database if not exists Activation_code')
    conn.select_db('Activation_code')
    cur.execute('create table code(id int,uuid varchar(50))')

    for i in range(len(rst)):
    	cur.execute('insert into code values(%s,%s)',(i ,rst[i]))
     
    conn.commit()
    cur.close()
    conn.close()
 
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


