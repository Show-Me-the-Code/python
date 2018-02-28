# --*-- encoding:utf-8 --*--
#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活
#码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
from __future__ import print_function
import random,sys
def activecode(cc,cl):
    codechart='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for cc in range(0,cc):
        s=[random.choice(codechart) for i in range(cl)]
        print(''.join(s))

if __name__ =='__main__':
    activecode(20,32)
