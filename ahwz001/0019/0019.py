#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0019
* by ahwz001
* 2017/9/16
* Thanks for this project. I learned a lot here.
"""

import xlrd
import json
from lxml import etree



def read_xls(fromfile):
    book = xlrd.open_workbook(fromfile)
    sheet = book.sheet_by_name('numbers')
    data = []
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        line = [int(sheet.cell_value(i, j)) for j in range(cols)]
        data.append(line)
    # print data
    return json.dumps(data, ensure_ascii = False)


def to_xml(data, tofile):
    root = etree.Element('root')
    stu = etree.SubElement(root, 'numbers')
    stu.append(etree.Comment(u'数字信息'))
    stu.text = data
    tree = etree.ElementTree(root)
    tree.write(tofile, encoding = 'utf-8', pretty_print = True, \
        xml_declaration = True)

    
if __name__ == '__main__':
    fromfile = 'numbers.xls'
    tofile = 'numbers.xml'
    data = read_xls(fromfile)
    to_xml(data, tofile)