#coding=utf-8
__author__ = 'tonnytwo'

'''第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？'''

import random
for a in xrange(0,200):
    str1 = ""
    for b in xrange(0,4):
        str1 = str1 + str(random.randint(0,9))
    print str1
