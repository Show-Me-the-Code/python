# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-03-26 16:35:51
Edit time: 2015-03-26 16:36:43
File name: 0003.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""

import sys
import os
import redis

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from q0001 import a0001

def add_to_redis(count):
    code_list = a0001.generate_activation_code(count)
    r = redis.Redis(host='localhost', port=6379, db=0)
    for index, i in enumerate(code_list):
        r.set(index, i)
        print index, i

if __name__ == '__main__':
    add_to_redis(200)
