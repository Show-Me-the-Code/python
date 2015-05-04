# -*- coding: utf-8 -*-
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
# using sina app
# test page:http://mccatcivitas.sinaapp.com/showmecode2
import sae.const
import MySQLdb
import uuid


def create_code(number=200):
    result = []
    while True is True:
        temp = str(uuid.uuid1()).replace('-', '')
        if not temp in result:
            result.append(temp)
        if len(result) is number:
            break
    return result


def insertCode(code, table='app_mccatcivitas.showmethecode'):
    conn = MySQLdb.connect(
        host=sae.const.MYSQL_HOST,
        user=sae.const.MYSQL_USER,
        passwd=sae.const.MYSQL_PASS,
        port=int(sae.const.MYSQL_PORT),
        charset='utf8')
    cur = conn.cursor()
    cur.execute("""insert into %s values('%s')""" % (
        table, code))
    conn.commit()
    cur.close()
    conn.close()


def selectCodes(table='app_mccatcivitas.showmethecode'):
    connection = MySQLdb.connect(
        host=sae.const.MYSQL_HOST,
        user=sae.const.MYSQL_USER,
        passwd=sae.const.MYSQL_PASS,
        port=int(sae.const.MYSQL_PORT),
        init_command='set names utf8')
    cur = connection.cursor()
    cur.execute("""select * from %s""" % (table))
    result = []
    rows = cur.fetchall()
    for row in rows:
        result.append(str(row[0]))
    return result


def cleanUp(table='app_mccatcivitas.showmethecode'):
    connection = MySQLdb.connect(
        host=sae.const.MYSQL_HOST,
        user=sae.const.MYSQL_USER,
        passwd=sae.const.MYSQL_PASS,
        port=int(sae.const.MYSQL_PORT),
        init_command='set names utf8')
    cur = connection.cursor()
    try:
        cur.execute("""drop table %s""" % (table))
    except Exception, e:
        print e
    connection.commit()
    cur.execute(
        """create table %s (code char(32) not null primary key)""" % (table))
    connection.commit()
    cur.close()
    connection.close()


def Process():
    cleanUp()
    code = create_code()
    for c in code:
        insertCode(c)
    result = selectCodes()
    return result
