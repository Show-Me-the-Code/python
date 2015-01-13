#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-12 17:22:35
# @Last Modified by:   30987
# @Last Modified time: 2015-01-12 22:33:53

#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import uuid
import MySQLdb

def creat_code(number=20):
	result = []
	while True is True:
		tem=str(uuid.uuid1()).replace('-','')
		if not tem in result:
			result.append(tem)
		if len(result) is number:
			break
	return result

def coont_db(result):
	num = len(result)
	db= MySQLdb.connect('localhost','root','','python',charset='utf8')
	cur = db.cursor()

	try:
		db= MySQLdb.connect('localhost','root','','python',charset='utf8')
		cur = db.cursor()
		print "OK"
		for i in xrange(num):
			cur.execute('insert into code (code_num) values("%s")' % (result[i]))
		db.commit()
	except:
		print "数据库连接错误!"
		db.rollback()
	db.close()



if __name__ == '__main__':
	coont_db(creat_code())
