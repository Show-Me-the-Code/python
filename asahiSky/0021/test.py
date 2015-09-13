import os
from hashlib import sha256
from hmac import HMAC


def encrypt_password(password, salt=None):

    if salt is None:
        salt = str(os.urandom(8))

    salt = salt.encode('utf-8')
    assert 8 == len(salt)
    if isinstance(password, str):
        password = password.encode('UTF-8')


    result = password
    for i in range(10):
    	result = HMAC(result,salt,sha256).digest()

    return salt+result


print(encrypt_password('Hty980204'))
