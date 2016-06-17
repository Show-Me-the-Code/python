#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中。'''

__author__ = 'Drake-Z'

import os
import re
from collections import OrderedDict
import xlwt

def read_data(data):
    c = OrderedDict([])
    re_xuhao = re.compile(r'"([\d]+)":')            
    re_yuansu = re.compile(r'\[(.*?)\]')            
    a = re_xuhao.findall(data)                      #得到序号
    b = re_yuansu.findall(data)                 #得到具体数据
    for m, n in zip(a, b):                          #将数据转为Dict
        n = re.split(r',', n)
        n[0] = n[0][1:-1]                            #去除引号
        c[m] = n
    writeFlie(c)

def writeFlie(dictdata):
    workbook = xlwt.Workbook(encoding = 'utf-8')                #创建工作薄
    worksheet = workbook.add_sheet('My Worksheet')              #创建表
    num = list(dictdata.keys())                                                    #得到序号
    for i in range(0, 3):
        worksheet.write(i, 0, label = num[i])
        for m in range(0, 4):
            worksheet.write(i, m+1, label = dictdata[num[i]][m])
    workbook.save('0014/student.xls')

if __name__ == '__main__':
    file = open('0014/student.txt', 'r', encoding='utf-8')
    read_data(file.read())