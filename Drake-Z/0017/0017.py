#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
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
</root>'''

__author__ = 'Drake-Z'

import os
import xlrd

def xmlwrite(hangshu):
    L = []
    L.append(r'<?xml version="1.0" encoding="UTF-8"?>')
    L.append(r'<root>')
    L.append(r'<students>')
    L.append(r'<!-- ')
    L.append(r'    学生信息表')
    L.append(r'    "id" : [名字, 数学, 语文, 英文]')
    L.append(r'-->')
    L.append(r'{')
    data = xlrd.open_workbook('student.xls')
    table = data.sheets()[0]
    for i in range(0, hangshu):
        a = '"%s" : ["%s", %s, %s, %s],' % (table.cell(i,0).value, table.cell(i, 1).value, table.cell(i, 2).value, table.cell(i, 3).value, table.cell(i, 4).value)
        L.append(r'    %s' % a)
    L.append(r'}')
    L.append(r'</students>')
    L.append(r'</root>')
    a = '\n'.join(L)
    f = open('students.xml', 'w')
    f.write(a)
    f.close()
    print(a)
    return 0

hangshu = 3
xmlwrite(hangshu)