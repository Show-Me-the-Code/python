import mysql.connector
import uuid

config={
    'host':'127.0.0.1',
    'user':'root',
    'password':'',
    'port':3306,
    'database':'class',
    'charset':'utf8'
    }

try:
    cnn=mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print ('connect fails!'.format(e))

print cnn

class sql_struct():
    def __init__(self,config):
        self.config=config

    def conn_sql(self):
        try:
            conn=mysql.connector.connect(**self.config)
        except mysql.connector.Error as e:
            print ('connect fails!'.format(e))
        self.conn=conn
        

    def conn_execute(self, sql_string, data):
        cursor=self.conn.cursor()
        cursor.execute(sql_string);
       # try:
          #  if data is '':
          #      cursor.execute(sql_string);
           # elif type(data) is tuple:
           #     cursor.execute(sql_string, data);
          #  elif type(data) is dict:
          #      cursor.execute(sql_string, data)
       # except mysql.connector.Error as e:
        #    print('fails{}'.format(e));
    def sql_close(self):
        self.conn.close()

class gene_keys():
    def __init__(self,num):
        self.num = num;
        self.list = [];

    def gene_list(self):
        for i in range(self.num):
            key=uuid.uuid1();
            self.list.append(str(key).replace('-',''));

    def return_list(self):
        return self.list;

g=gene_keys(2);
g.gene_list();
keys_list=g.return_list();
#db=sql_struct(config);
#db.conn_sql();
print cnn
#sql create table ``
sql_create_table='create table `keyss1` (\
    `source` varchar(10),\
    `key` varchar(20)\
)';

#db.conn_execute(sql_create_table, '');
cursor=cnn.cursor()
sql_insert2="insert into keyss1 (source, key) values ('orange', '20')"
cursor.execute(sql_insert2);
#db.sql_close()
#for key in keys_list:
#    data=('uuid', key);
    #print key
    #db.conn_execute(sql_insert2,'')
 #   cursor=cnn.cursor()
#    cursor.execute(sql_insert2);
#db.sql_close()








    
#cursor=cnn.cursor()
#print sql_create_table
#try:
 #   cursor.execute(sql_create_table)
#except mysql.connector.Error as e:
 #   print('create table fails'.format(e));
