'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
import random
import pymysql
def creat_num(num,long):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    b = []
    for i in range(num):
        a = ''
        for j in range(long):
            a += random.choice(str)
        b.append(a)
    return b

def InsertIntoMysql(codelist):
    # 打开数据库连接
     db = pymysql.connect(host='127.0.0.1',user='root',passwd='919824467',db='mysql')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cur = db.cursor()
    #数据库语句
    cur.execute('CREATE DATABASE IF NOT EXISTS code')
    cur.execute('USE code')
    cur.execute('''CREATE TABLE IF NOT EXISTS num(
                    id INT NOT NULL AUTO_INCREMENT,
                    code VARCHAR(32) NOT NULL,
                    PRIMARY KEY(id) )''')
            for num in codelist:
                cur.execute('INSERT INTO num(code) VALUES(%s)',(num))
                cur.connection.commit()
    db.close()

InsertIntoMysql(creat_num(200,10))