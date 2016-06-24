#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-13
# Blog: morningchen.com
import random
import string


#  字典域 由数字和字母（包括大小写）组成
FIELD = string.digits + string.letters


def generate(n, many=1, where=None):
    """
        生成many组随机码
    """
    def getCode(n):
        """
            得到n位激活码
        """
        return "".join(random.sample(FIELD, n))
    gene = [getCode(n) for i in range(many)]
    return gene


def writeIn(n, many, where):
    """
        写入文件 并按顺序排列
    """
    count = 1
    for i in generate(n, many):
        with open(where, "a") as boom:
            boom.write(str(count).rjust(3)+"  "+i+"\n")
        count += 1


if __name__ == '__main__':
    writeIn(20, 200, "coupon.txt")
