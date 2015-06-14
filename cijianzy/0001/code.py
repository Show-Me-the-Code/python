#!/usr/bin/python
#coding:utf-8
# Author: cijianzy
# Created Time: 2015年06月14日 星期日 17时43分18秒

from uuid import uuid4
def get_key(num):
    key_list = [str(uuid4()) for i in range(num)]
    return key_list 
print get_key(200)

