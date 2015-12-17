#!/usr/bin/env python3

import hmac, hashlib, os

def encrypt_passwd(password, salt=None):
    if salt is None:
        salt = str(os.urandom(8)).encode('utf-8')
    if isinstance(password, str):
        password = password.encode('utf-8')

    result = password
    for i in range(10):
        result =  hmac.HMAC(result, salt, hashlib.sha256).digest()
    return salt+result
    
if __name__=="__main__":
    e_passwd = encrypt_passwd(b'hello')
    print(e_passwd)
