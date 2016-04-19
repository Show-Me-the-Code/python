# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql


# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("CREATE DATABASE IF NOT EXISTS pymysql;")
cursor.execute("USE pymysql;")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS active_code(code VARCHAR(255));")

with open("active_code.txt", "r") as f:
    while True:
        s = f.readline().strip()
        # print(s)
        if s == "":
            break
        cursor.execute("INSERT INTO active_code (code) values(%s)", [s])

db.commit()
#cursor.execute("USE pymsql")
cursor.execute("SELECT * FROM active_code")

# 使用 fetchone() 方法获取一条数据库。
#data = cursor.fetchone()

#print("Database version : %s " % data)

# 关闭数据库连接
db.close()
