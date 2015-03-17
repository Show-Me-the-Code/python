#!/bin/env python
# -*- coding: utf-8 -*- 

#要填json坑，前面写的代码，json部分是网上找的，还没有完全理解，尤其是相关的字符串编码没有实践
#抽空了解下从xls文件读取数据的库
#xls -> json -> xml 是我的思路，当然也可以尝试下直接xls -> xml
#主要还是比较看重json的应用。有时候感觉看了别人的代码，不自己用另一种方式实现，（即使变得复杂啰嗦）还是别人的代码

#导入模块
import xlrd
#这个是系统自带的，如果安装lxml遇到问题可以使用这个
import xml.etree.ElementTree as ET
from xml.dom import minidom


def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)        #通过索引获取xls文件第0个sheet
    nrows = table.nrows
    d = {}
    for i in range(nrows):
        d[str(i+1)] = table.row_values(i)[1:]  #取编号后的数据，以列表形式存在字典对应的值中
    return d
 
def write_xml(d):
    doc = minidom.Document()
    root = doc.createElement("root")
    doc.appendChild(root)
    students = doc.createElement("students")
    root.appendChild(students)
    students.appendChild(doc.createComment('    学生信息表\n    "id" : [名字, 数学, 语文, 英文]'))
    for i in d:
        d[i][0] = d[i][0].encode('utf-8')
    #有一种无奈叫做我懒得玩了，python2你是个好人
    content = doc.createTextNode(str(d))
    students.appendChild(content)
    f = file("student.xml","w")
    doc.writexml(f)
    f.close()


def main():
    d = read_xls('student.xls')
    print(d)
    write_xml(d)


if __name__ == '__main__':
    main()
