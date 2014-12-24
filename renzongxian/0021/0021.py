# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-24
# Python 3.4

"""

第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？
请使用 Python 对密码加密。

"""

import uuid
import hashlib


def encrypt_password(password):
    salt = uuid.uuid4().hex
    result = password
    for i in range(10):
        result = hashlib.sha256(salt.encode() + result.encode()).hexdigest()
    return salt + ':' + result

if __name__ == '__main__':
    pw = input('Please input your password:')
    print("The password stored in the database is:" + encrypt_password(pw))

