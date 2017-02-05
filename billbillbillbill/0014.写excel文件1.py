#!/usr/bin/env python
#coding: utf-8
import os
import json
import xlwt
from collections import OrderedDict

# 存放文件的目录
filepath = '/home/bill/Desktop'

def run():
    os.chdir(filepath)
    # 读取文件内容
    with open('student.txt') as f:
        content = f.read()
    # 转为json, 注意转化后的dict的元素位置和转化前可能会不一致，因此要使用OrderedDict
    d = json.loads(content, object_pairs_hook=OrderedDict)
    file = xlwt.Workbook()
    # 添加sheet
    table = file.add_sheet('test')
    for row, i in enumerate(list(d)):
        table.write(row, 0, i)
        for col, j in enumerate(d[i]):
            table.write(row, col+1, j)
    file.save('student.xls')

if __name__ =="__main__":
    run()
