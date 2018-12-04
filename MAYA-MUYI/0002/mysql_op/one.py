import pymysql
import  string
import random

forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        yield Re

def save_code():
    conn = pymysql.connect(db='tests', user='root', passwd='299521', host='localhost')
    cursor = conn.cursor()
    codes = generate_code(200, 20)
    for code in codes:
        print(code)
        sql = "INSERT INTO code(code) VALUES ('%s')" %code
        cursor.execute(sql)
    conn.commit()
    cursor.close()

if __name__ == '__main__':

    save_code()