#!/usr/bin/env python

'''
	It can save the contents of the file to the mysql database.
'''

import os
import random
import MySQLdb
#import string

f = open(os.getcwd()+'\\2','w')
for x in range(200):
	words = [chr(a) for a in range(65,91)]+[chr(a) for a in range(97,122)]+[str(a) for a in range(0,11)]
	# It is equal to string.ascii_letters + string.digits
	slices = random.sample(words,10)
	#temp = str(slices)
	temp = "".join(slices)+'\n'
	#print temp
	f.write(temp)
f.close()

f = open(os.getcwd()+'\\2','r')
words = f.readlines()
try:
	conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '******', port = 3306)#connet to your local database of mysql

	cur = conn.cursor()

	conn.select_db('python')

	count = cur.executemany('insert into test(name) values(%s)',words)#executemant need two parameters sql statement and list

	conn.commit()#commit the implementation results
	cur.close()#close the cursor
	conn.close()# close the connect
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])

