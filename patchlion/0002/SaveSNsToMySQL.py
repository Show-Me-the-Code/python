# -*- coding: utf-8 -*-
__author__ = 'PatchLion'

import pymysql

sns = []

with open('../0001/sns.txt', 'rt') as f:
    for line in f.readlines():
        sn = line.strip()
        sns.append(sn)

print(sns)

def insertToDB(sns):
    if(len(sns) == 0):
        return

    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root',password='root', db='python')
    cur = conn.cursor()
    try:
        cur.execute('DELETE FROM sns')
        conn.commit()

        for sn in sns:
            cur.execute('INSERT INTO sns VALUE ("%s")' % sn)
            conn.commit()
        conn.close()

        print('Done!')
    except:
        conn.rollback()


insertToDB(sns)