import pymysql

conn = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = '',
        db = 'test'
        )           #连接数据库
cur = conn.cursor()     #创建游标
ret = 0     #返回影响row
with open('coupons.txt') as f:
    coupons = f.readlines()
    for coupon in coupons:
        ret += cur.execute('insert into jihuoma(mima) values(%s)', coupon)

conn.commit()   #提交
cur.close()     #关闭指针对象
conn.close()    #关闭连接对象

print (ret)
