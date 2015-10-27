#!/usr/bin/python
# coding=utf-8

"""
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xml version="1.0" encoding="UTF-8"?>
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
</root>
"""

import xlrd
import json
from lxml import etree


def read_exl(file_name):
    exl = xlrd.open_workbook(file_name)
    exl_sheet = exl.sheet_by_name('city')
    data = {}
    for i in range(exl_sheet.nrows):
        data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1]
    return json.dumps(data, encoding='utf-8')

def save_to_xml(data, new_file_name):
    root = etree.Element('root')
    students = etree.SubElement(root, 'citys')
    students.append(etree.Comment(u"""城市信息"""))
    students.text = data

    student_xml = etree.ElementTree(root)
    student_xml.write(new_file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    content = read_exl('city.xls')
    save_to_xml(content, 'city.xml')
