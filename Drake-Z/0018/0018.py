#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：
<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!-- 
    城市信息
-->
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
</citys>
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
    output = codecs.open('city.xml','w','utf-8')
    root = etree.Element('root')
    city_xml = etree.ElementTree(root)
    city = etree.SubElement(root, 'city')
    city.append(etree.Comment('城市信息'))
    city.text = str(data)
    output.write(etree.tounicode(city_xml.getroot()))
    output.close()

if __name__ == '__main__':
    file = 'city.xls'
    a = read_xls(file)
    save_xml(a)