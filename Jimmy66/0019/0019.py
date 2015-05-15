#!/bin/env python
# -*- coding: utf-8 -*- 

#导入模块
import xlrd
import xml.etree.ElementTree as ET
from xml.dom import minidom


def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)        #通过索引获取xls文件第0个sheet
    nrows = table.nrows
    l = []
    for i in range(nrows):
        l.append(table.row_values(i))  #list用append方法
    return l
 
def write_xml(l):
    doc = minidom.Document()
    root = doc.createElement("root")
    doc.appendChild(root)
    numbers = doc.createElement("numbers")
    root.appendChild(numbers)
    numbers.appendChild(doc.createComment('\n    数字信息\n'))
    #list就是好，数字就是爽
    content = doc.createTextNode(str(l))
    numbers.appendChild(content)
    #file函数有空了解下，之前一直都用with open 直接解决的问题，无论是读还是写
    f = file("numbers.xml","w")
    doc.writexml(f)
    f.close()


def main():
    l = read_xls('numbers.xls')
    print(l)
    write_xml(l)


if __name__ == '__main__':
    main()
