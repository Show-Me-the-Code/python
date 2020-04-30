# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
# 学习了mysql的连接
with open('../01/coupon1.txt', 'r') as fh:
    coupon_list = []
    for line in fh:
        coupon_list.append(line.replace('\n', ''))
    print(coupon_list)

# 存入mysql
import mysql.connector

connect = mysql.connector.connect(user='root', password='lawrence34', database='test')
cursor = connect.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS coupons (id varchar(20) primary key, coupon_number varchar(20))')
for k, v in enumerate(coupon_list):
    cursor.execute('INSERT INTO coupons VALUE (%s,%s)', [k + 1, v])
connect.commit()

cursor.execute('SELECT * FROM coupons')
values = cursor.fetchall()
print(values)
cursor.close()
connect.close()

