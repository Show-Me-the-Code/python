import os
from hashlib import sha256
from hmac import HMAC


def encrypt_password(password,salt=None):
    if salt is None:
        salt = os.urandom(8)    # 64 bits.

    if isinstance(salt,str):
        salt = salt.encode('utf-8')

    result = password.encode('utf-8')
    for i in range(10):
        result= HMAC(result,salt,sha256).digest()
    return salt+result

if __name__ == '__main__':
    passwd = input("please input your password: \n")
    print(encrypt_password(passwd, 'a'))
