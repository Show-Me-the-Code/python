#coding=utf-8

import uuid

import MySQLdb

"""
002, 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中
"""


class ActivationCode(object):
    def __init__(self, code_count, database, username, host='localhost', port=3306, password=''):
        self._host = host
        self._username = username
        self._password = password
        self._database = database
        self._port = port

        self.codes = self._generate_activation_code(code_count)
        #print self.codes


    def _get_mysql_instance(self):
        params = {
                  'host': self._host,
                  'user': self._username,
                  'passwd': self._password,
                  'db': self._database,
                  'port': self._port,
        }
        return MySQLdb.connect(**params)


    def _generate_activation_code(self, count):
        code_list = []
        for i in xrange(count):
            code = str(uuid.uuid4()).replace('-', '').upper()
            if not code in code_list:
                code_list.append(code)

        return code_list


    def store_to_mysql(self):
        if self.codes:
            conn = self._get_mysql_instance()

            try:
                cur = conn.cursor()
                
                # clear old datas
                cur.execute('delete from code')

                # insert mutilple code
                for code in self.codes:
                    cur.execute("insert into code(code) values('%s')" % code)

                conn.commit()
                cur.close()
                conn.close()

                return True
            except MySQLdb.Error,e:
                conn.rollback()
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])

        return False


    def print_activation_code(self):
        conn = self._get_mysql_instance()

        try:
            cur = conn.cursor()
            cur.execute('select code from code')

            results = cur.fetchall()
            for row in results:
                print row[0]
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])


if __name__ == "__main__":
    active_code = ActivationCode(200, database='Test', username='root')
    if active_code.store_to_mysql():
        active_code.print_activation_code()
