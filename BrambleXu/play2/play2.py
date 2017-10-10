# -*- coding:utf-8 -*-
#**第 0002 题**：将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

import MySQLdb

def store_mysql(filepath):
    db = MySQLdb.connect(host="localhost", user = "xu", passwd = "1234", db = "ShowMeTheCode")
    cursor = db.cursor()

    #判断表是否存在
    cursor.execute('show tables in ShowMeTheCode;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
            print "the table is already exist"
    if not findtables:
        cursor.execute('''
                    CREATE TABLE code(
                    id INT NOT NULL AUTO_INCREMENT,
                    code VARCHAR(10)
                    PRIMARY KEY (id));
        ''')

    f = open(filepath, 'rb')
    for line in f.readlines():
        coupon = line.strip() #用strip把\n去掉
        cursor.execute("INSERT INTO code (code) VALUES (%s);", [coupon]) # coupon会报错，格式问题，插入数据库里的数据必须要变为list，所以用【coupon]

    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    store_mysql('Running_result.txt')
