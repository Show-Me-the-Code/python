# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-03-26 15:53:17
Edit time: 2015-03-26 16:32:23
File name: 0001.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import uuid

"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者
优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
print 'import 0001'

def generate_activation_code(count):
    code_list = []
    # for i in xrange(count):
    while len(code_list) < count:
        code = str(uuid.uuid4()).replace('-', '').upper()
        if code not in code_list:
            code_list.append(code)

    return code_list


if __name__ == "__main__":
    code_list = generate_activation_code(200)
    for code in code_list:
        print code
