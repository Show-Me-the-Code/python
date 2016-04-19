#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-17 12:11:29
# @Last Modified by:   key
# @Last Modified time: 2015-11-17 17:21:24

#--------------------------------
#--第 0001 题：
#--做为 Apple Store App 独立开发者.
#--你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python如何生成 200 个激活码（或者优惠券）？
#--------------------------------

import random

#digit 优惠码位数
#count 优惠码数量
def make_promo_code(digit,count):
    base = ord('A')
    results = set()
    alphanums = [str(i) for i in range(10)] + [chr(base+i) for i in range(26)]
    with open('result','w') as f:
        while len(results) < 200:
            temp = ''.join(random.choice(alphanums) for j in range(digit))
            if temp not in results:
                f.write(temp+'\r\n')
                results.add(temp)

if __name__ == '__main__':
    make_promo_code(8,200)


