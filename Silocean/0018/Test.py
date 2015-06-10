# -*-coding:utf-8-*-
__author__ = 'Tracy'

import xlrd,json,sys
reload(sys)
sys.setdefaultencoding('utf8')

with xlrd.open_workbook('city.xls', 'w') as f:
    table = f.sheet_by_index(0)

rows = table.nrows
cols = table.ncols
dic = {}
for row in range(rows):
    dic[str(row+1)] = table.row_values(row)[1]

s = json.dumps(dic, ensure_ascii=False, indent=4)

content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<citys>\n<!--\n    城市信息\n-->\n'

content = content + s + '\n</citys>\n</root>'

with open('city.xml', 'w') as f:
    f.write(content)