# -*- coding: utf-8 -*- 
import uuid

def gen( num):
    assert isinstance(num, int) == True
    assert num > 0
    rst = []
    while True:
        temp = str(uuid.uuid1()).replace('-', '')
        if temp not in rst:
            rst.append(temp)
            num = num - 1
            if num == 0:
                break
    return rst

rst = gen(200)
for i in rst:
    print i
