import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('coupons.db');
    cursor = conn.cursor();
    with open('./Sources/coupons', 'r') as f:

        coupons_ = f.readlines();

        try:
            cursor.execute('create table coupons (code varchar(16) primary key)');
        except:
            cursor.execute('DROP TABLE coupons');
            cursor.execute('create table coupons (code varchar(16) primary key)');
        finally:
            for item in coupons_:
                cursor.execute('insert into coupons (code) values (?)', (item,));
            cursor.close();
            conn.close();

    f.close();

    print 'successfully put data in sqlite';
