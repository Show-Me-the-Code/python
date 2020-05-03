# 第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
# 学习了哈希算法-单向函数，输入lawrence34（b形式），经过function，输出一串bite，无法逆推所以加密
# 参考https://www.pythoncentral.io/hashing-strings-with-python/
import hashlib
import uuid


def hash_password(ipt):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha3_224(ipt.encode()).hexdigest() + ':' + salt
    return hashed_password


def check_password(ipt_password, hashed_password):
    password, salt = hashed_password.split(':')
    return hashlib.sha3_224(ipt_password.encode()).hexdigest() == password


if __name__ == '__main__':
    new_password = input('Please set a password')
    password = hash_password(new_password)
    print('Password Set, your password is %s' % password)
    print('------------')
    a = input('Please enter your password')
    if check_password(a, password):
        print('Logged in')
    else:
        print('Sorry, incorrect password')
