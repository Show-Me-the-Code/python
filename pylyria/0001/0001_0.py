# -*- coding: utf-8 -*-
#!/usr/bin/env python
#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random
import string

def activation_code(id,length=16):
    prefix = hex(int(id))[2:]+'V'
    length = length - len(prefix)
    chars=string.ascii_uppercase+string.digits
    return prefix + ''.join([random.choice(chars) for i in range(length)])

def get_id(code):
    return str(int(code.upper(), 16))

if __name__ == '__main__':
    for i in range(10, 500, 23):
        code = activation_code(i)
        id_hex = code.split('L')[0]
        id  = get_id(id_hex)
        print code,id
