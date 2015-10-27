#!/usr/bin/python
# coding=utf-8

"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

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
</root>
"""

import xlrd
import json
from lxml import etree


def read_exl(file_name):
    exl = xlrd.open_workbook(file_name)
    exl_sheet = exl.sheet_by_name('student')
    data = {}
    for i in range(exl_sheet.nrows):
        data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1:]
    return json.dumps(data, encoding='utf-8')

def save_to_xml(data, new_file_name):
    root = etree.Element('root')
    students = etree.SubElement(root, 'students')
    students.append(etree.Comment(u"""学生信息表 "id" : [名字, 数学, 语文, 英文]"""))
    students.text = data

    student_xml = etree.ElementTree(root)
    student_xml.write(new_file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    content = read_exl('student.xls')
    save_to_xml(content, 'student.xml')
