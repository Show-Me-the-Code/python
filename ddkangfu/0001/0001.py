#coding=utf-8

import uuid

"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

def generate_activation_code(count):
    code_list = []
    for i in xrange(count):
        code = str(uuid.uuid4()).replace('-', '').upper()
        if not code in code_list:
            code_list.append(code)

    return code_list


if __name__ == "__main__":
    code_list = generate_activation_code(200)
    for code in code_list:
        print code