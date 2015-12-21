
#!/usr/bin/python
#coding=utf-8
__author__ = 'tonnytwo'
import MySQLdb
import random

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="123456", # your password
                      db="pythontest") # name of the data b

cur = db.cursor()
for a in xrange(0,200):
    str1 = ""
    for b in xrange(0,4):
        str1 = str1 + str(random.randint(0,9))
    print str1
    sql =  "insert into test VALUES ('%s','%s')" % (a,str1)
    print sql
    cur.execute(sql)
db.commit()

try:
   cur.execute("""
      select * from test
   """)
   result = cur.fetchall()
   print result
finally:
    cur.close()

db.close()

