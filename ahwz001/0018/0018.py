#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0018
* by ahwz001
* 2017/9/16
* Thanks for this project. I learned a lot here.
"""

import xlrd
import json
from lxml import etree


def read_xls(fromfile):
    book = xlrd.open_workbook(fromfile)
    sheet = book.sheet_by_name('city')
    data = {}
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        kv = sheet.cell_value(i, 1)
        key = str(int(sheet.cell_value(i, 0)))
        # print key, kv
        data[key] = kv
    # print data
    return json.dumps(data, ensure_ascii = False, sort_keys = True)


def to_xml(data, tofile):
    root = etree.Element('root')
    stu = etree.SubElement(root, 'citys')
    stu.append(etree.Comment(u'城市信息'))
    stu.text = data
    tree = etree.ElementTree(root)
    tree.write(tofile, encoding = 'utf-8', pretty_print = True, \
        xml_declaration = True)

    
if __name__ == '__main__':
    fromfile = 'city.xls'
    tofile = 'city.xml'
    data = read_xls(fromfile)
    to_xml(data, tofile)
    