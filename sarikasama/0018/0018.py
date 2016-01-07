#!/usr/bin/env python3
#convert from xls to xml

import xlrd, json
from lxml import etree
from collections import OrderedDict

def xls2xml(xls_name):
    with xlrd.open_workbook(xls_name) as wb:
        ws = wb.sheet_by_index(0)
    table = OrderedDict()
    for i in range(ws.nrows):
        key = int(ws.row_values(i)[0])
        value = ws.row_values(i)[1]
        table[key] = value

    with open("city.xml", 'w') as f:
        root = etree.Element("root")
        e_root = etree.ElementTree(root)
        e_citys = etree.SubElement(root, 'citys')
        e_citys.text = '\n'+str(json.dumps(table, indent=4, ensure_ascii=False))+'\n'
        e_citys.append(etree.Comment('\n    城市信息\n'))
        f.write('<?xml version="1.0" encoding="UTF-8"?>'+etree.tounicode(e_root.getroot()))

if __name__=="__main__":
    xls2xml('city.xls')
