import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf8')


file = xlwt.Workbook(encoding='utf-8')
table = file.add_sheet('numbers', cell_overwrite_ok=True)
txt = open('numbers.txt').read()
json_txt = json.loads(txt)
for x in range(len(json_txt)):
    for y in range(len(json_txt[x])):
        table.write(x, y, json_txt[x][y])
file.save('numbers.xls')
