#!/usr/bin/env python
#coding: utf-8
import string, random

#激活码中的字符和数字
field = string.letters + string.digits

#获得四个字母和数字的随机组合
def getRandom():
    return "".join(random.sample(field,4))

#生成的每个激活码中有几组
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

#生成n组激活码
def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    print generate(200)