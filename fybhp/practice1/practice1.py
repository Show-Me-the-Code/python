# -*- coding:utf-8 -*-
import re
import string
import random

map = {}
#pattern = re.compile(r'([a-z0-9A-Z]{4}-){3}([a-z0-9A-Z]{4})')
#这个函数定义的很精髓
def id_generator(size=4, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    #[random.choice(chars) for _ in range(size)]为列表解析
    #(random.choice(chars) for _ in range(size))为生成器，其对内存更友好
    list = []
    for i in range(4):
        a = ''.join(random.choice(chars) for _ in range(size))
        list.append(a)
    return list
for i in range(200):
    id = '-'.join(id_generator())
    while id in map.values():
        id = '-'.join(id_generator())
    map[i] = id
print map
