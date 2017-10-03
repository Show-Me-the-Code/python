#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0021
* by ahwz001
* 2017/10/03
* Thanks for this project. I learned a lot here.
* Open http://pythoncentral.io/hashing-strings-with-python/ for more information.
"""

import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt + password).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt + user_password).hexdigest()
 

def main():
    new_pass = raw_input('please enter a password: ')
    hashed_password = hash_password(new_pass)
    print('the string to store in the database is:'  + hashed_password)
    old_pass = raw_input('please enter a password: ')
    if check_password(hashed_password, old_pass):
        print('You entered the right password')
    else:
        print('I am sorry but the password does not match')


if __name__ == '__main__':
    main()


