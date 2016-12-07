#reference: https://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb as mysqldb

def store_reldb():
    db = mysqldb.connect(host = 'localhost', user = 'chris', passwd = '1314', \
                         db = 'show_me_the_code')
    cursor = db.cursor()

    #Create a table
    cursor.execute('drop table if exists verify_info')
    sql = '''
        create table verify_info (
        id int not null auto_increment primary key,
        verify_code char(20)
        )'''
    cursor.execute(sql)

    
    #Insert data
    f = open('result.txt', 'rb')
    for line in f:
        verify_code = line.strip()        
        sql = 'insert into verifY_info(verify_code) values ("%s");' % \
              (verify_code)
        cursor.execute(sql)
    try:        
        db.commit()
    except:
        db.rollback()
        f.close()
        print 'Error happened when inserting data'
    f.close()
    db.close()
    
if __name__ == '__main__':
    store_reldb()
