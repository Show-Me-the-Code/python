# Python Databases Note - MySQL


### install and setting
```
sudo apt-get install mysql-server
sudo apt-get install python-mysqldb
mysql -u root -p
# create a user and table in mysql
> CREATE DATABASE testdb;
> CREATE USER 'testuser'@'localhost' IDENTIFIED BY '123';
> USE testdb;
> GRANT ALL ON testdb.* TO 'testuser'@'localhost';
```


### _mysql module

The _mysql module implements the MySQL C API directly.  
Not compatible.

Fetch version

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys

try:
    con = _mysql.connect('localhost', 'test', '123', 'testdb')
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print "MySQL version: %s" % \
        result.fetch_row()[0]
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()
```


### MySQLdb module

MySQLdb is a thin Python wrapper around _mysql.


1. con = mdb.connect(...)
2. cur = con.cursor()   // **get cursor**
3. cur.execute("SELECT * FROM xxx")
4. cur.executemany("INSERT INTO xxx VALUES(%s, %s)", value_list)
4. except mdb.Error, e  // **remember this**
5. cur.rowcount
6. cur.fetchone()       // **return one**
7. cur.fetchall()       // **return a list**
8. cur = con.cursor(mdb.cursors.DictCursor) // **dictionary cursor, we can refer to the data by their column names**
9. desc = cur.description   // **table column names**


Fetch version.

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

try:
    con = mdb.connect('localhost', 'test', '123', 'testdb');
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()
    print "Database version : %s " % ver
    
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
    if con:    
        con.close()
```

Create a table and populate it with some data

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'test', '123', 'testdb');

with con:   # automatically release con
    cur = con.cursor()
    # Above can be `with mdb.connect(...) as cur`

    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
```

Retrieving data

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'test', '123', 'testdb');

with con: 
    cur = con.cursor()      # con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()   # if is DictCursor rows is a dict
    for row in rows:
        print row

    # or fetch one by one
    # for i in range(cur.rowcount):
    #     row = cur.fetchone()
    #     print row
```


### Some resources:  
[MySQLdb User's Guide](http://mysql-python.sourceforge.net/MySQLdb.html)  
[python-mysqldb API](http://mysql-python.sourceforge.net/MySQLdb-1.2.2/)  
[StackOverflow-How do I connect to a MySQL Database in Python?](http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python)  
[Good start:Zencode](http://zetcode.com/db/mysqlpython/) (I use this :smile:)  

