# -*- coding:utf8 -*-
# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-06
# Python 2.7, MySQL-python does not currently support Python 3

"""

第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

"""

import uuid
import MySQLdb


def generate_key():
    key_list = []
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-', ''))
    return key_list


def write_to_mysql(key_list):
    # Connect to database
    db = MySQLdb.connect("localhost", "test", "test1234", "testDB")

    # Use function cursor() to open the cursor operation
    cursor = db.cursor()

    # If the table exists, delete it
    cursor.execute("drop table if exists ukey")

    # Create table
    sql = """create table ukey (
            key_value char(40) not null
            )"""
    cursor.execute(sql)

    # Insert data
    try:
        for i in range(200):
            cursor.execute('insert into ukey values("%s")' % (key_list[i]))
        # Commit to database
        db.commit()
    except:
        # Rollback when errors occur
        db.rollback()

    # Close database
    db.close()


if __name__ == '__main__':
    write_to_mysql(generate_key())

