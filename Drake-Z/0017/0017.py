#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>'''

__author__ = 'Drake-Z'

import xlrd,codecs
from lxml import etree
from collections import OrderedDict

def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    c = OrderedDict()
    for i in range(table.nrows):
        c[table.cell(i,0).value] = table.row_values(i)[1:]
    return c

def save_xml(data):
    output = codecs.open('student.xml','w','utf-8')
    root = etree.Element('root')
    student_xml = etree.ElementTree(root)
    student = etree.SubElement(root, 'student')
    student.append(etree.Comment('学生信息表\n\"id\": [名字，数学，语文，英语]'))
    student.text = str(data)
    output.write(etree.tounicode(student_xml.getroot()))
    output.close()

if __name__ == '__main__':
    file = 'student.xls'
    a = read_xls(file)
    save_xml(a)











