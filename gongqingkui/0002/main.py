'''
sudo /etc/init.d/mysql start
mysql -u root -p
create database pymysql_db default charset utf8 collate utf8_general_ci;
use pymysql_db
CREATE TABLE `activecode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activecode` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
pip instll pymysql
'''
from __future__ import print_function
import pymysql
import random,sys


def activecode(cl):
    codechart='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=[random.choice(codechart) for i in range(cl)]
    return (''.join(s))

def activecodes(cc,cl):
    for cc in range(0,cc):
        s=activecode(cl)
        print(''.join(s))

def getcursor():
    conn = pymysql.connect(host='192.168.1.3', port=3306, user='root', passwd='root', db='test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn,cursor

def saveactivecode(activecode):
    sql="insert into activecode(activecode)values('{0}');".format(activecode)
    #print(sql)
    cursor.execute(sql)
    
    
if __name__ =='__main__':
    conn,cursor = getcursor()
    #saveactivecode('123')
    for i in range(20):
        saveactivecode(activecode(32))
    conn.commit()
    cursor.close()
    conn.close()
