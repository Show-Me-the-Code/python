__author__ = 'PyBeaner'
import pymysql.cursors


def save_to_mysql(coupons):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='user',
                                     passwd='passwd',
                                     db='db',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            select_sql = "SELECT coupon FROM coupons where coupon='%s'"
            insert_sql = "INSERT INTO coupons VALUES (%s);"
            for coupon in coupons:
                cursor.excute(select_sql, (coupon,))
                result = cursor.fetchone()
                if result:
                    continue

                cursor.excute(insert_sql, (coupon,))

        connection.commit()
    finally:
        connection.close()
