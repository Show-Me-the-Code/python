#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
    数字信息
-->
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
</numbers>
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
    output = codecs.open('numbers.xml','w','utf-8')
    root = etree.Element('root')
    numbers_xml = etree.ElementTree(root)
    numbers = etree.SubElement(root, 'numbers')
    numbers.append(etree.Comment('城市信息'))
    numbers.text = str(data)
    output.write(etree.tounicode(numbers_xml.getroot()))
    output.close()

if __name__ == '__main__':
    file = 'numbers.xls'
    a = read_xls(file)
    save_xml(a)