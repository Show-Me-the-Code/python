#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中。'''

__author__ = 'Drake-Z'

import os
import re
from collections import OrderedDict
import xlwt

def shuju(data, re1, re2):
    c = OrderedDict([])
    re_xuhao = re.compile(r'%s' % re1)            
    re_yuansu = re.compile(r'%s' % re2)            
    a = re_xuhao.findall(data)                      #得到序号
    if len(a)==0:
        for d in range(0, hangshu):
            a.append(d)
    b = re_yuansu.findall(data)                 #得到具体数据
    for m, n in zip(a, b):                          #将数据转为Dict
        n = re.split(r',', n)
        c[m] = n
    writeFlie(c, hangshu, lieshu)

def writeFlie(dictdata, hangshu, lieshu):
    workbook = xlwt.Workbook(encoding = 'utf-8')                #创建工作薄
    worksheet = workbook.add_sheet('My Worksheet')              #创建表
    num = list(dictdata.keys())                                                    #得到序号
    for i in range(0, hangshu):
        for m in range(0, lieshu):
            worksheet.write(i, m, label = dictdata[num[i]][m])
    workbook.save('numbers.xls')

if __name__ == '__main__':
    file = open('numbers.txt', 'r', encoding='utf-8')
    hangshu = 3
    lieshu = 3
    re1 = '%'
    re2 = '\[(.*?)\]'
    shuju(file.read(), re1, re2)