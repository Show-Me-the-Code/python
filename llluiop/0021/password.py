#!/usr/bin/env python
#-*- coding: utf-8-*-



import os
from hashlib import sha256
from hmac import HMAC

def encode(password):
    salt = os.urandom(8)
    print salt

    result = password.encode("utf-8")

    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return result

if __name__ == "__main__":
    password = "password"
    print encode(password)