# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
    相关模块/库 : pymysql
        1. http://www.runoob.com/python3/python3-mysql.html
'''
import random, string, time, math, uuid, pymysql

chars = string.ascii_letters + string.digits

def gen1():
    key = ''.join(random.sample(chars, 10))
    #key2 = ''.join(random.choice(chars) for i in range(10))
    return key

def gen2():
    key = math.modf(time.time())[0]
    return key

def gen3():
    return uuid.uuid4()

def dbp():
    db = pymysql.connect('localhost', 'root', '1213', 'python')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS CODE")
    sql = """CREATE TABLE CODE (
        app_code CHAR(100) NOT NULL
    )"""
    cursor.execute(sql)
    return db, cursor

if __name__ == '__main__':
    db, cursor = dbp()
    for i in range(200):
        add_code = "INSERT INTO CODE(app_code) VALUES ('%s')" % gen2()
        # print(add_code)
        try:
            cursor.execute(add_code)
            db.commit()
        except:
            db.rollback()
    db.close()
    print('finish')

