#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0021
* by ahwz001
* 2017/10/03
* Thanks for this project. I learned a lot here.
* Open http://zhuoqiang.me/password-storage-and-python-example.html for more information. 
"""

import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])


if __name__ == '__main__':
    hashed = encrypt_password('secret password')
    if validate_password(hashed, 'secret password'):
        print "the password is correct!"
    else:
        print "I am sorry but the password does not match"
