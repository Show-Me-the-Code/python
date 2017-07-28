#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0002
* by ahwz001
* 2017/7/22
* thanks this project, I learned some very useful Program.
"""


import MySQLdb
import random

KEY_LEN = 8
KEY_ALL = 200
BASE_STR = '0123456789ABCDEF'


def key_gen():
    '''make single  key code'''
    keylist = [random.choice(BASE_STR) for i in range(KEY_LEN)]
    return ''.join(keylist)


def key_num(num, result=None):
    '''make num keys and save to file "the_keys_bill.txt", return a list of keys.'''
    if result is None:
        result = []
    while len(result) < num:
        t = key_gen()
        if t not in result:
            result.append(t)
            # Adding key that are not duplicates.
        else:
            continue
    # for i in range(num):
    #     result.append(key_gen())
    with open('the_keys_bill.txt','w') as fobj:
        t = '\n'.join(result)
        fobj.write(t)
    return result


class mysql_init(object):
    '''a class that connect to mysql database'''

    def __init__(self,conn):
        self.conn = None

    def connect(self):
        self.conn = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = '123456',
            db = 'test',
            )

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()


def CreateTable(conn):
    # conn = dbconn.cursor()
    sql_create = "CREATE TABLE `user_key` (`id` int primary key,`key` varchar(50) NOT NULL,`Flag` varchar(10))"
    conn.execute(sql_create)


def DropTable(conn):
    # conn = dbconn.cursor()
    conn.execute("DROP TABLE IF EXISTS `user_key`")


def InsertDatas(conn):
    # conn = dbconn.cursor()
    insert_sql = "insert into user_key values(%s, %s, %s)"
    key_list = key_num(KEY_ALL)
    row = 0
    for v in key_list:
        row += 1
        conn.execute(insert_sql,[row, v, 'True'])


def QueryData(conn):
    '''query data from user_key.'''
    sql = "select * from user_key"
    conn.execute(sql)
    rows = conn.fetchall()
    printResult(rows)


def DeleteData():
    del_sql = "delete from user_key where id=2"
    conn.execute(del_sql)


def printResult(rows):
    if rows is None:
        print "rows None"
    for row in rows:
        print row


def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)    
    InsertDatas(conn)
    QueryData(conn)
    dbconn.commit()
    dbconn.close()


if __name__ == '__main__':
    dbconn = mysql_init(None)
    process()
