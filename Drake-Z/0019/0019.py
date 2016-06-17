#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
    数字信息
-->
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
</numbers>
</root>'''

__author__ = 'Drake-Z'

import os
import xlrd

def xmlwrite(file, hangshu):
    L = []
    L.append(r'<?xml version="1.0" encoding="UTF-8"?>')
    L.append(r'<root>')
    L.append(r'<numbers>')
    L.append(r'<!-- ')
    L.append(r'    数字信息')
    L.append(r'-->')
    L.append(r'[')
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    for i in range(0, hangshu):
        a = '[%s, %s, %s],' % (table.cell(i, 0).value, table.cell(i, 1).value, table.cell(i, 2).value)
        L.append(r'    %s' % a)
    L.append(r']')
    L.append(r'</numbers>')
    L.append(r'</root>')
    a = '\n'.join(L)
    f = open('numbers.xml', 'w')
    f.write(a)
    f.close()
    print(a)
    return 0

file = 'numbers.xls'
hangshu = 3
xmlwrite(file, hangshu)