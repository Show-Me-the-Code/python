# -*- coding: utf-8 -*-
import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf8')


file = xlwt.Workbook(encoding='utf-8')
table = file.add_sheet('student', cell_overwrite_ok=True)
txt = open('student.txt').read()
json_txt = json.loads(txt)
for x in range(len(json_txt)):
    table.write(x, 0, x + 1)
    for y in range(len(json_txt[str(x + 1)])):
        table.write(x, y + 1, json_txt[str(x + 1)][y])
file.save('students.xls')
