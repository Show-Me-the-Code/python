# -*- coding: utf-8 -*-
import json
import xlrd
from lxml import etree

testfile = 'numbers.xls'
savename = 'numbers.xml'
sheetname = 'number'

def to_xml(data):
    root = etree.Element('root')
    stu = etree.SubElement(root, 'numbers')
    comm = etree.Comment(u'数字信息')
    stu.append(comm)

    stu.text = data
    tree = etree.ElementTree(root)
    tree.write(savename, encoding = 'utf-8', pretty_print = True, \
               xml_declaration = True)

def read_excel(testfile):
    book = xlrd.open_workbook(testfile)
    sheet = book.sheet_by_name(sheetname)
    data = []
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        line = [int(sheet.cell_value(i, j)) for j in range(cols)]
        data.append(line)
    return json.dumps(data)
    

if __name__ == '__main__':
    data = read_excel(testfile)
    to_xml(data)
    
