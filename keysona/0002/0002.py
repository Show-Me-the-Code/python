#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-17 13:38:09
# @Last Modified by:   key
# @Last Modified time: 2015-11-17 17:24:22

#--------------------------------------
#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
#--------------------------------------

import random
import MySQLdb

#digit 优惠码位数
#count 优惠码数量
def make_promo_code(digit,count):
    base = ord('A')
    results = set()
    alphanums = [str(i) for i in range(10)] + [chr(base+i) for i in range(26)]
    #数据库连接
    conn = MySQLdb.connect(host='localhost',user='root',passwd='12345678',db='test')
    cur = conn.cursor()
    cur.execute("create table promo_code(id int auto_increment primary key,promo_code varchar(10))")
    conn.commit()
    while len(results) < 200:
        promo_code = ''.join(random.choice(alphanums) for j in range(digit))
        if promo_code not in results:
            cur.execute("insert into promo_code(promo_code) values('{0}')".format(promo_code))
            results.add(promo_code)
    conn.commit()
    #关闭数据库
    cur.close()
    conn.close()

if __name__ == '__main__':
    make_promo_code(8,200)
