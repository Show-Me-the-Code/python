# -*- coding: utf-8 -*-
"""
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""
import pymysql
__author__ = 'Chris5641'


def code2sql():
    f = open('ActivationCode.txt', 'r')
    conn = pymysql.connect(user='root', passwd='password')
    cursor = conn.cursor()
    cursor.execute('create database if not exists accode')
    cursor.execute('use accode')
    cursor.execute('create table accode(id int auto_increment primary key, code varchar(10))')
    for line in f.readlines():
        cursor.execute('insert into accode (code) values (%s)', [line.strip()])
    conn.commit()
    f.close()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    code2sql()
