# using sina app
# test page:http://mccatcivitas.sinaapp.com/showmecode2
import sae.const
import MySQLdb
import uuid

HOST = sae.const.MYSQL_HOST
USER = sae.const.MYSQL_USER
PASSWD = sae.const.MYSQL_PASS
PORT = int(sae.const.MYSQL_PORT)
CHARSET = 'utf8'
INIT_COMMAND = 'set names utf8'


def make_connection(host=HOST, user=USER, passwd=PASSWD, port=PORT, charset=CHARSET, init_command=INIT_COMMAND):
    return MySQLdb.connect(host=host, user=user, passwd=passwd, port=port, charset=charset, init_command=init_command)


def create_code(number=200):
    result = []
    while True is True:
        temp = str(uuid.uuid1()).replace('-', '')
        if not temp in result:
            result.append(temp)
        if len(result) is number:
            break
    return result


def insertCode(code, table='app_mccatcivitas.showmethecode'):
    conn = make_connection()
    cur = conn.cursor()
    cur.execute("""insert into %s values('%s')""" % (
        table, code))
    conn.commit()
    cur.close()
    conn.close()


def selectCodes(table='app_mccatcivitas.showmethecode'):
    connection = make_connection()
    cur = connection.cursor()
    cur.execute("""select * from %s""" % (table))
    result = []
    rows = cur.fetchall()
    for row in rows:
        result.append(str(row[0]))
    return result


def cleanUp(table='app_mccatcivitas.showmethecode'):
    connection = make_connection()
    cur = connection.cursor()
    try:
        cur.execute("""drop table %s""" % (table))
    except Exception, e:
        print e
    connection.commit()
    cur.execute(
        """create table %s (code char(32) not null primary key)""" % (table))
    connection.commit()
    cur.close()
    connection.close()


def Process():
    cleanUp()
    code = create_code()
    for c in code:
        insertCode(c)
    result = selectCodes()
    return result
