# -*-coding:utf-8-*-
__author__ = 'Tracy'

import xlrd,json,sys
reload(sys)
sys.setdefaultencoding('utf8')

with xlrd.open_workbook('numbers.xls', 'w') as f:
    table = f.sheet_by_index(0)

rows = table.nrows
cols = table.ncols

lists = []

for row in range(rows):
    list = []
    for x in table.row_values(row):
        list.append(x)
    lists.append(list)
s = json.dumps(lists,ensure_ascii=False, indent=4)
content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<numbers>\n<!--\n    数字信息\n-->\n'
content = content + s + '\n</numbers>\n</root>'

with open('numbers.xml', 'w') as f:
    f.write(content)
