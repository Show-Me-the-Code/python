'''
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如下所示：
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
'''

import xlrd, json
import xmltodict

def read_excel(filepath):
    exl = xlrd.open_workbook(filepath)
    sheet = exl.sheet_by_index(0)
    data = {}
    for row in range(sheet.nrows):
        data[sheet.row_values(row)[0]] = sheet.row_values(row)[1:]
    data_1 = {}
    data_1['root'] = data
    print(data_1)
    xml = xmltodict.unparse(data_1)
    print(xml)

if __name__ == '__main__':
    read_excel('../14/students.xls')
