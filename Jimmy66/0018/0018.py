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
    d = {}
    for i in range(nrows):
        d[str(i+1)] = table.row_values(i)[1]   #才发现之前忘记+1了
    return d
 
def write_xml(d):
    doc = minidom.Document()
    root = doc.createElement("root")
    doc.appendChild(root)
    citys = doc.createElement("citys")
    root.appendChild(citys)
    citys.appendChild(doc.createComment('\n    城市信息\n'))
    for i in range(1,4):
        d[str(i)] = d[str(i)].encode('utf-8')   #之前忘记修改[0]，导致python理解为切片，然后报错了，还好有交互式环境帮助排错理解
    #嘛，又发现一个问题，字典是乱序的，所以直接转的话，就算顺序是正确的，也是碰巧，所以还是用JSON比较好吧，先完成，以后再慢慢学习优化吧
    content = doc.createTextNode(str(d))
    citys.appendChild(content)
    f = file("city.xml","w")
    doc.writexml(f)
    f.close()


def main():
    d = read_xls('city.xls')
    print(d)
    write_xml(d)


if __name__ == '__main__':
    main()
