#coding=utf-8
import os,MySQLdb,re
path = os.path.split(os.path.realpath(__file__))[0]+"/"
f = open(path+"code.txt","r")
A = f.read()
db = MySQLdb.connect("127.0.0.1","root","root","0002" )
cursor = db.cursor()
arr = re.split("\s+",A)
cursor.execute("DROP TABLE IF EXISTS CODE")
sql = """CREATE TABLE CODE (
         no INT,
		content text
		 )"""
cursor.execute(sql)
for i in range(len(arr)):
	if i:
		sql = """INSERT INTO `code` SET `no`=%s,`content`='%s'"""%(i,arr[i])
		cursor.execute(sql)