#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
分析
其实要生成激活码(邀请码)也是很简单的事, 比如随机生成.或者使用GUID,UUID等,非常简单

但是我们得考虑存入以及验证的问题.

这里我参考产生唯一随机码的方法分析。这篇文章的思路:

主键+随机码的方式.

这种方法优点：使用也比较简单，不用直接去查询数据库，而最大的优点是查询的时候，可以根据邀请码直接得到主键id, 然后根据id去数据库查询(速度很快)，再比较查询出来的邀请码和用户提交的邀请码是否一致。

生成:id(数据库primary key )->16进制 + "L(标识符)" +随机码
获取id:获取16进制的id再转回10进制
"""


import random
import string

def activation_code(id,length=10):
    '''
    id + L + 随机码
    string模块中的3个函数：string.letters，string.printable，string.printable
    '''
    prefix = hex(int(id))[2:]+ 'L'
    length = length - len(prefix)
    chars=string.ascii_letters+string.digits
    return prefix + ''.join([random.choice(chars) for i in range(length)])

def get_id(code):
    ''' Hex to Dec '''
    return str(int(code.upper(), 16))

if __name__=="__main__":
    for i in range(10,500,35):
        code = activation_code(i)
        id_hex = code.split('L')[0]
        id  = get_id(id_hex)
        print code,id
