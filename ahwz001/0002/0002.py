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


def ReadKeys():
    """Read keys form file,and return as a list."""
    res = []
    with open("the_keys_bill.txt") as fobj:
        for line in fobj:
            t = line.strip()
            res.append(t)
    return res

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
    sql_create = "CREATE TABLE `user_key` (`id` int primary key,`active_key` varchar(50) NOT NULL,`Flag` varchar(10))"
    conn.execute(sql_create)


def DropTable(conn):
    # conn = dbconn.cursor()
    conn.execute("DROP TABLE IF EXISTS `user_key`")


def InsertDatas(conn):
    # conn = dbconn.cursor()
    insert_sql = "insert into user_key values(%s, %s, %s)"
    key_list = ReadKeys()
    row = 0
    for v in key_list:
        row += 1
        conn.execute(insert_sql,[row, v, 'True'])


def PrintAll(conn):
    '''query data from user_key.'''
    sql = "select * from user_key"
    conn.execute(sql)
    rows = conn.fetchall()
    printResult(rows)


def printResult(rows):
    if rows is None:
        print "rows None"
    for row in rows:
        print row


def DeleteData(conn):
    del_sql = "delete from user_key where id=2"
    conn.execute(del_sql)


def VerifyKey(conn,test_key='25C492DF'):
    """Veriy a keycode is valid or not. return True or False"""
    t = '\'' + test_key + '\''
    verify_sql = "select * from user_key where active_key=" + t
    conn.execute(verify_sql)
    res = conn.fetchone()
    if res and res[2] == 'True':
        # make sure the table user_key has test_key and the Flag is True.
        print "the record is:"
        print res
        print "the test_key is valid ! Congratulations!"
        return True
    else:
        print "the test_key is invalid ! Please try another one !"
        return False


def UseActiveKey(conn,test_key='25C492DF'):
    """Determine if the activation code is valid, if it is valid and Ready to use it, then update 
    the Flag of this active_key to False to Avoid reuse."""
    print "the test_key is: %s" % test_key
    t = '\'' + test_key + '\''
    update_sql = "update user_key set Flag='False' where active_key=" + t
    if VerifyKey(conn,test_key):
        print "Are you sure to use the test_key ?"
        print "Press any key to continue, or CTRL-C to abort ?"
        raw_input('>')
        # update the Flag
        conn.execute(update_sql)
        t = '\'' + test_key + '\''
        query_sql = "select * from user_key where active_key=" + t
        conn.execute(query_sql)
        print "the test_key's Flag is updated sucsessful!"
        print conn.fetchone()
    else:
        pass


def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)    
    InsertDatas(conn)
    # PrintAll(conn)
    # VerifyKey(conn)
    UseActiveKey(conn,test_key='25C492DF')
    print '\nA case for another test_key'
    UseActiveKey(conn,test_key='ABCDEF12')
    DeleteData(conn)
    dbconn.commit()
    dbconn.close()


if __name__ == '__main__':
    dbconn = mysql_init(None)
    process()
