## 第 0002 题
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

## 步骤
1、create a database TESTDB
2、create a table EMPLOYEE in TESTDB
This table has fields FIRST_NAME, LAST_NAME, AGE, SEX and INCOME
User ID "testuser" and password "test123" are set to access TESTDB

Python 3的参考链接: [MySQL Database Access python3的参考链接](https://www.tutorialspoint.com/python3/python_database_access.htm)


注意：python3不再支持mysqldb，使用 pymysql和mysql.connector
关于python2 mysqldb的使用方式参考如下链接
reference: [Python MySQL Database Access](https://www.tutorialspoint.com/python/python_database_access.htm)

## mac上安装mysql

```
brew install mysql-connector-c 
pip install MySQL-python   或者  pip install PyMySQL
```

## 问题
### 问题1

```
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'localhost' ([Errno 61] Connection refused)")
```
1、首先，通过如下链接查看mysql是否启动：
https://stackoverflow.com/questions/6885164/pymysql-cant-connect-to-mysql-on-localhost

2、在 `/usr/local/etc/` 下创建或修改 my.cnf

```
[client]
port = 3306
socket = /tmp/mysql.sock
default-character-set = utf8

[mysqld]
collation-server = utf8_unicode_ci
character-set-server = utf8
init-connect ='SET NAMES utf8'
max_allowed_packet = 64M
bind-address = 127.0.0.1
port = 3306
socket = /tmp/mysql.sock
innodb_file_per_table=1

[mysqld_safe]
timezone = '+0:00'
```

3、 `mysql.server start` 来启动

```
▶ mysql.server start
Starting MySQL
.. SUCCESS!
```

如果要关闭的话

```
▶ mysql.server stop
Shutting down MySQL
.... SUCCESS!
```

### 问题2

```
pymysql.err.OperationalError: (1044, "Access denied for user 'test'@'%' to database 'testdb'")
```

解决参考这个链接：

https://stackoverflow.com/questions/6445917/connect-failed-access-denied-for-user-rootlocalhost-using-password-yes

实践：

```
▶ mysql -u root -h localhost

mysql> CREATE USER 'test'@'localhost' IDENTIFIED BY 'test123';
Query OK, 0 rows affected (0.00 sec)
mysql> CREATE DATABASE testdb;
Query OK, 1 row affected (0.00 sec)
mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'test'@'localhost';
Query OK, 0 rows affected (0.01 sec)
mysql> quit;
Bye
```

用设置好的用户名 test 和密码 test123 登录

```
▶ mysql -u test -p -h localhost
Enter password:
```

登录成功。

- 其他
 1. one.py需要事先建立数据表
 2. two.py是用代码执行包括数据表的建立