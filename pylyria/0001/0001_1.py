# -*- coding: utf-8 -*-
#!/usr/bin/env python
#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random
import string

def activation_code(chars = string.ascii_uppercase + string.digits, length=16):
    return ''.join([random.choice(chars) for i in range(length)])

if __name__ == '__main__':
    code_collection = set()
    for i in range(200):
        code = activation_code()
        if code not in code_collection:
            code_collection.add(code)
        else:
            continue
