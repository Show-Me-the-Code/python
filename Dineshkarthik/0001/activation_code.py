#!/usr/local/bin/python
#coding=utf-8
__author__ = 'Dineshkarthik'

#0001 Title: As Apple Store App independent developer, you engage in limited-time promotion for your application to generate activation code (or coupon), how to use Python to generate 200 activation code (or coupon)?

import uuid

def act_code(count):
    f = open('code.txt', 'wb')
    for i in range(count):
        s = str(uuid.uuid4().get_hex().lower()[0:8])
        f.write(''.join(s) + '\n')
    f.close()

if __name__ == '__main__':
    act_code(200)
