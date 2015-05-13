import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf8')


file = xlwt.Workbook(encoding='utf-8')
table = file.add_sheet('city', cell_overwrite_ok=True)
txt = open('city.txt').read()
json_txt = json.loads(txt)
for x in range(len(json_txt)):
    table.write(x, 0, x + 1)
    table.write(x, 1, json_txt[str(x + 1)])
file.save('city.xls')