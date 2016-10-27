# -*- coding:utf-8 -*-
# I use this file to test the database method
'''
I want to creat a data base that named xu, student_id is 1, name is bramble, sex is male
'''

import MySQLdb

if __name__ == "__main__":
    # connect to the database
    db = MySQLdb.connect("localhost","xu","1234","test" )
    cursor = db.cursor()

    name = 'bramble'
    sex = 'youguess'

    #insert
    cursor.execute('insert into student_table (name, sex) value (%s, %s)', (name, sex))

    #connect.commit()
    #select
    cursor.execute('select * from student_table')
    db.commit()

    row = cursor.fetchall()

    #output
    for i in row:
        print(i)

    #disconnect database
    db.close()
