# -*-coding:utf-8-*-
__author__ = 'Tracy'

import uuid

f = open('keys.txt', 'w')

for i in range(200):
    f.write(str(uuid.uuid1())+"\n")

f.close()

