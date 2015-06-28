#!/usr/bin/env python
#coding=utf-8

"""第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示："""

__author__ = 'tonnytwo'
import json
import xlwt
import xlrd

def Test():
    f = open("./students.txt","r")
    text = f.read()
    js = json.loads(text)
    print type(js)
    print js["1"]

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('student')
    ww = 0
    for key in js:
        ws.write(ww,0,key)
        hh = 1
        for key2 in js[key]:
            ws.write(ww,hh,key2)
            hh = hh + 1
        ww = ww+1
    #ws.write(2, 1, 1)
    #ws.write(2, 2, xlwt.Formula("A3+B3"))

    wb.save('example.xls')
Test()









