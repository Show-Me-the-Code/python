import time, os, json, MySQLdb, HTMLParser, cgi
def SQL_init():
	db = MySQLdb.connect("127.0.0.1","root","root","0024" )
	return db.cursor()
def SQL_max(new=None):
	cursor = SQL_init()
	if new != None
		sql="""UPDATE `max` SET `max`=%d WHERE `pro`='max'"""%new
		cursor.execute(sql)
		return True
	else:
		sql="""SELECT * FROM `max` WHERE `pro`='max'"""
		cursor.execute(sql)
		return cursor.fetchall()[0][1]
def SQL_in(task):
	max = SQL_max()
	
def SQL_out():
	cursor = SQL_init()
	sql = """SELECT * FROM `code`"""
	cursor.execute(sql)
	return cursor.fetchall()