#coding: utf-8
import random
from hashlib import sha256
from hmac import HMAC


def set_password(raw_password, salt=None):
    if salt is None:
        salt = sha256(str(random.random())).hexdigest()[-8:]
    if isinstance(raw_password, unicode):
        raw_password = raw_password.encode('utf-8')
    # password = sha256('%s%s' % (salt, raw_password)).hexdigest()
    password = HMAC(salt, raw_password, sha256).hexdigest()
    return ('%s$%s' % (salt, password))


def check_password(raw_password, enc_password):
    salt = enc_password.split('$')[0]
    return enc_password == set_password(raw_password, salt)


if __name__ == '__main__':
    raw_password1 = 'hehe'
    raw_password2 = 'test'
    salt = '12345678'
    enc_password1 = set_password(raw_password1)
    enc_password2 = set_password(raw_password2, salt)
    print 'enc_password1:%s' % enc_password1
    print 'enc_password2:%s' % enc_password2
    print check_password(raw_password1, enc_password1)
    print check_password(raw_password2, enc_password2)
