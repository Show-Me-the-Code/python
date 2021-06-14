# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import pymysql

# 打开连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='my_test', charset='utf8mb4')
# 使用cursor() 获取操作游标
cursor = conn.cursor()
# create table
sql = 'create table if not exists activate_code (code_id char(36) not null)'
# 执行sql语句
cursor.execute(sql)

with open('../0001/txt/activate_code.txt', 'r') as f:
    activate_codes = f.readlines()
    for code in activate_codes:
        cursor.execute("insert into activate_code values ('%s')" % str(code))
# 关闭 close()
cursor.close()
# 提交数据
conn.commit()
# 关闭连接
conn.close()
