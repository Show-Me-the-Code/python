#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。'''

__author__ = 'Drake-Z'

import hashlib
from collections import defaultdict
db = {}
db = defaultdict(lambda: 'N/A')                     #去掉登录可能产生的KeyError

def get_md5(password):
    a = hashlib.md5()
    a.update(password . encode('utf-8'))
    return (a.hexdigest())

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    b = get_md5(password + username + 'the-Salt' )
    if b==db[username]:
        return True
    else:
        return False
a = input('注册输入用户名：')
b = input('注册输入密码：')
register(a, b)
a = input('登录输入用户名：')
b = input('登录输入密码：')
print(login(a, b))