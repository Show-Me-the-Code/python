# 0002

uuids=[]

import uuid

for i in range(1,200):
    '''
    uuid.uuid1()
    uuid.uuid1
    因为不加括号的结果是函数本身，
    所以显示出来是一个 function；
    加了括号以后是得到的结果是执行函数之后的返回值，
    也就是计算出来的激活码。
    显示中多出了 UUID()
    是因为打印一个对象的时候会用对象里的 __repr__ 函数进行格式化后再输出，
    而 __repr__ 一般会返回一个可以作为代码执行的字符串
    （如果用 print 或者 str() 的话则是用 __str__ 函数格式化，
    就没有 UUID() 了）
    '''
    uuids.append(str(uuid.uuid4()))

# 安装mysql
# sudo apt-get install mysql-client mysql-server
# python3下
# sudo apt-get install python3-dev libmysqlclient-dev
# pip3 install mysqlclient
# python2下
# pip install mysql-python

# MySqlDB官网只支持Python3.4，这里Python3.5使用第三方库PyMysql连接Mysql数据库。
import pymysql
import os

db=pymysql.connect("localhost","root",os.getenv("Mysql_password"),"candy")

cursor=db.cursor()
create_sql="""
        create table random(
        id INT PRIMARY KEY ,
        random CHAR(50)
        )
        """
cursor.execute(create_sql)

try:
    for i,value in enumerate(uuids):
        insert_sql="insert into random(id,random) VALUES ('%s','%s')" %(i,value)
        cursor.execute(insert_sql)
    db.commit()
except:
    db.rollback()

db.close()




