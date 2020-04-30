#!/usr/bin/python
# coding=utf-8

"""
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，如下图所示：
"""

import json, xlwt

text = '''
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}'''

data = json.loads(text)
print(data)

wb = xlwt.Workbook()
ws = wb.add_sheet('cities', cell_overwrite_ok=True)
for index, (k,v) in enumerate(data.items()):
    ws.write(index, 0, k)
    ws.write(index,1,v)
wb.save('cities.xls')