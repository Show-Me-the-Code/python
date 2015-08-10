# 生成激活码

import random
import string

charset = string.ascii_letters + string.digits


def generate_keyset(length, num, as_tuple=False):
    if as_tuple:
        return [(generate_key(16),) for i in range(num)]
    else:
        return [generate_key(length) for i in range(num)]


def generate_key(length):
    return ''.join(random.sample(charset, length))


if __name__ == '__main__':
    key = generate_keyset(16, 200)
