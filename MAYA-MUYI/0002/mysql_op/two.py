import pymysql

def store_mysql():
    conn = pymysql.connect(db='tests', user='root', passwd='299521', host='localhost')
    cursor = conn.cursor()

    # create a table
    cursor.execute("drop table if exists verify_info")
    sql = """create table verify_info (
            id int not null auto_increment primary key,
            verify_code varchar(20))"""
    cursor.execute(sql)

    f = open('str.txt', 'r')
    for line in f.readlines():
        sql = "INSERT INTO verify_info(verify_code) VALUES ('%s')" % line
        cursor.execute(sql)
    try:
        conn.commit()
    except:
        conn.rollback()
        f.close()
        print("error happend when inserting data")
    f.close()
    conn.close()

if __name__ == '__main__':
    store_mysql()
