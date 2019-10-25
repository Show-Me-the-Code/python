from random import randint
import MySQLdb
def makeCode(length,number):
    code = []
    code_set = set(code)
    code_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    limit = len(code_map)
    while(len(code_set)<number):
        this_code = ""
        for i in range(length):
            this_code += code_map[randint(0,limit-1)]
        code.append(this_code)
        code_set = set(code)

    return code_set

def insertDatebase(code):
    db = MySQLdb.Connect("localhost","root","","pythonmysql")
    cursor = db.cursor()
    sql = """INSERT INTO my_practice
         VALUES ('%s')""" % code
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

if __name__ == '__main__':
    codes = makeCode(20,200)
    for code in codes:
        insertDatebase(code)