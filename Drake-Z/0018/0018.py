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

import os
import xlrd

def xmlwrite(file, hangshu):
    L = []
    L.append(r'<?xml version="1.0" encoding="UTF-8"?>')
    L.append(r'<root>')
    L.append(r'<citys>')
    L.append(r'<!-- ')
    L.append(r'    城市信息')
    L.append(r'-->')
    L.append(r'{')
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    for i in range(0, hangshu):
        a = '"%s" : "%s",' % (table.cell(i, 0).value, table.cell(i, 1).value)
        L.append(r'    %s' % a)
    L.append(r'}')
    L.append(r'</citys>')
    L.append(r'</root>')
    a = '\n'.join(L)
    f = open('city.xml', 'w')
    f.write(a)
    f.close()
    print(a)
    return 0

file = 'city.xls'
hangshu = 3
xmlwrite(file, hangshu)