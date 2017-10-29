import os
import hashlib


def encrypt_password(password):
    salt = os.urandom(8)
    result = hashlib.sha256(password.encode()+salt).hexdigest()
    return salt, result


def check_password(user, password):
    salt = user['salt']
    return hashlib.sha256(password.encode()+salt).hexdigest() == user['password']

user = {'password': '', 'salt': b''}
raw_password = 'password'
user['salt'], user['password'] = encrypt_password(raw_password)
result = check_password(user, raw_password)
print(result)
