#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0017
* by ahwz001
* 2017/9/11
* Thanks for this project. I learned a lot here.
"""

import xlrd
import json
from lxml import etree


def read_xls(fromfile):
    book = xlrd.open_workbook(fromfile)
    sheet = book.sheet_by_name('student')
    data = {}
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        kv = []
        for j in range(1, cols):
            temp = sheet.cell_value(i,j)
            if isinstance(temp, float):
                kv.append(int(temp))
            else:
                kv.append(temp)
        key = str(int(sheet.cell_value(i, 0)))
        # print key, kv
        data[key] = kv
    # print data
    return json.dumps(data, ensure_ascii = False, sort_keys = True)


def to_xml(data, tofile):
    root = etree.Element('root')
    stu = etree.SubElement(root, 'students')
    stu.append(etree.Comment(u'学生信息表\n\t"id" : [名字, 数学, 语文, 英文]'))
    stu.text = data
    tree = etree.ElementTree(root)
    tree.write(tofile, encoding = 'utf-8', pretty_print = True, \
        xml_declaration = True)

    
if __name__ == '__main__':
    fromfile = 'student.xls'
    tofile = 'student.xml'
    data = read_xls(fromfile)
    to_xml(data, tofile)
    