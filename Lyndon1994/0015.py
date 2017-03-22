# -*- coding: utf-8 -*-
"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，如下图所示：
"""
import xlwt,json

with open('source/0015/city.txt','r') as f:
    data = json.load(f)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('city', cell_overwrite_ok=True)
    for index, (key, value) in enumerate(data.items()):
        sheet1.write(index, 0, key)
        sheet1.write(index, 1, value)
    workbook.save('source/0015/city.xls')