#coding=utf-8
import time, os, json, MySQLdb, HTMLParser, cgi
def SQL_init():
	db = MySQLdb.connect("127.0.0.1","root","root","0024" )
	return db.cursor()
def SQL_max(new=None):
	cursor = SQL_init()
	if new != None:
		sql="""UPDATE `max` SET `max`=%d WHERE `pro`='max'"""%new
		cursor.execute(sql)
		return True
	else:
		sql="""SELECT * FROM `max` WHERE `pro`='max'"""
		cursor.execute(sql)
		max = cursor.fetchall()[0][1]
		SQL_max(max+1)
		return max
def SQL_in(task):
	max = SQL_max()
	cursor = SQL_init()
	sql = """INSERT INTO `code` SET `id`=%d,`to`='%s';"""%(max, task)
	cursor.execute(sql)
	return True
def SQL_out():
	cursor = SQL_init()
	sql = """SELECT * FROM `code`"""
	cursor.execute(sql)
	return cursor.fetchall()
def SQL_del(id):
	cursor = SQL_init()
	sql = """DELETE FROM `code` WHERE `id`=%d"""%id
	cursor.execute(sql)
	return json.dumps(cursor.fetchall())
#-----------
Temp = """
<tr>
            <td class="task">%s</td>
            <td class="manage">
              <div align="center">
                <input type="submit" name="id-%d" id="delete" value="删除" />
              </div></td>
        </tr>
"""


def PageMake():
	Data = SQL_out()
	All = ""
	Data = sorted(Data,key=lambda a:a[0] )  
	for i in Data:
		#print i
		All+=Temp%(str(i[1]),int(i[0]))
	return All