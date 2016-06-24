#!/usr/bin/env python3
#convert from xls to xml

import xlrd, json
from lxml import etree

def xls2xml(xls_name):
    with xlrd.open_workbook(xls_name) as wb:
        ws = wb.sheet_by_index(0)
    table = []
    for i in range(ws.nrows):
        table.append(ws.row_values(i))

    with open("numbers.xml", 'w') as f:
        root = etree.Element("root")
        e_root = etree.ElementTree(root)
        e_numbers = etree.SubElement(root, 'numbers')
        e_numbers.text = '\n'+str(json.dumps(table, indent=4))+'\n'
        e_numbers.append(etree.Comment('\n    数字信息\n'))
        f.write('<?xml version="1.0" encoding="UTF-8"?>'+etree.tounicode(e_root.getroot()))

if __name__=="__main__":
    xls2xml('numbers.xls')
