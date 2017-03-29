#-*- coding:utf-8 -*-
import uuid
import pymysql

def generateActivationCode(num):
    codeList = []
    for i in range(num):
        code = str(uuid.uuid4()).replace('-','').upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace('-','').upper()
        codeList.append(code)

    return codeList

def storeInMysql(codelist):
    try:
        conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mysql')
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('CREATE DATABASE IF NOT EXISTS activation_code')
            cur.execute('USE activation_code')
            cur.execute('''CREATE TABLE IF NOT EXISTS code(

                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id)
                        )''')
            for code in codelist:
                cur.execute('INSERT INTO code(code) VALUES(%s)',(code))
                cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    storeInMysql(generateActivationCode(200))
    print('OK!')