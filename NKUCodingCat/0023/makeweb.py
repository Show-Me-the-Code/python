import time, os, json, MySQLdb, HTMLParser, cgi

def odd(src):
	return """<div class="odd">%s</div>"""%src
def nor(src):
	return """<div class="nor">%s</div>"""%src
def public(Name,TimeStamp,Content):
	return """<div class="text"><h3 class="NameType">%s @ %s</h3><pre>%s</pre></div>"""%(Name, time.ctime(TimeStamp),Content)
def Pack(Array):
	Count = 1
	pack = ""
	for i in Array:
		if not i:
			continue
		if Count%2 == 1:
			pack+=odd(public(i[0],i[1],cgi.escape(i[2])))
		else:
			pack+=nor(public(i[0],i[1],cgi.escape(i[2])))
		Count+=1
	return pack
#=========
def SQL_init():	
	db = MySQLdb.connect("127.0.0.1","root","root","0023" )
	return db.cursor()
def Stor_in(New):
	cursor = SQL_init()
	sql = """INSERT INTO `code` SET `Name`='%s',`TimeStamp`=%f,`Content`='%s'"""%(New["Name"],time.time(),New["Content"])
	cursor.execute(sql)
	return "Send Comment Success!"
def Stor_out(st=0,leng=50):
	cursor = SQL_init()
	sql = """SELECT * FROM `code` LIMIT %d,%d;"""%(st,(st+leng))
	cursor.execute(sql)
	return cursor.fetchall()