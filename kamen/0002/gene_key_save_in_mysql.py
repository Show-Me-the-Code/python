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



class sql_struct():
    def __init__(self,config):
        self.config=config

    def conn_sql(self):
        try:
            conn=mysql.connector.connect(**self.config)
        except mysql.connector.Error as e:
            print ('connect fails!{}'.format(e))
        self.conn=conn
        

    def conn_execute(self, sql_string, data):
        cursor=self.conn.cursor()
        #cursor.execute(sql_string);
        try:
            if data is '':
                cursor.execute(sql_string);
            elif type(data) is tuple:
                cursor.execute(sql_string, data);
            elif type(data) is dict:
                cursor.execute(sql_string, data)
        except mysql.connector.Error as e:
            print('fails{}'.format(e));
            
    def sql_close(self):
        self.conn.close()

    def sql_commit(self):
        self.conn.commit()

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
db=sql_struct(config);
db.conn_sql();
#print cnn

#sql create table ``
sql_create_table='create table `keyss1` (\
    `source` varchar(10),\
    `key` varchar(20)\
)';

sql_insert2=("insert into keyss1(source, keyss) values (%s, %s)")
for key in keys_list:
    data=('uuid', key);
    db.conn_execute(sql_insert2,data)
    
db.sql_commit();
db.sql_close()





