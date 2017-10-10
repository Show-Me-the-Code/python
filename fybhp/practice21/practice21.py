# -*-coding:utf-8-*-
import redis
from werkzeug.security import generate_password_hash, check_password_hash

#建立redis数据库连接.
db = redis.Redis(host = 'localhost',port = 6379,db = 0)

while True:
    option = raw_input(u'请选择：\n1.注册\n2.登陆\n')
    if option == '1':
        Username = raw_input(u'请输入用户名：')
        if db.exists(Username):
            print u'用户已存在。'
            continue
        Set_password = raw_input(u'请设置密码:')
        password_hash = generate_password_hash(Set_password)
        db.set(Username,password_hash)
    if option == '2':
        Username = raw_input(u'用户名：')
        password_hash = db.get(Username)
        password = raw_input(u'请输入密码：')
        if check_password_hash(password_hash,password):
            print u'登陆成功。'
        else:
            print u'用户名或密码错误。'

