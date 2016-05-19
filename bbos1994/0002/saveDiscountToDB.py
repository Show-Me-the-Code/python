#! /usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = 'TonyZhu'

import mysql.connector
import discount 

def saveToMySQL(discount_str):
	conn = mysql.connector.connect(user = 'root',password='password',database = 'Test')
	cursor = conn.cursor()
	cursor.execute('insert into discount values(%s)',[discount_str])
	count = cursor.rowcount

	conn.commit()
	cursor.close()
	return count

if __name__ == '__main__':
	discount_arr = discount.produce(3)
	for _discount in discount_arr:
		flag = True if saveToMySQL(_discount) == 1 else False
		print(flag)