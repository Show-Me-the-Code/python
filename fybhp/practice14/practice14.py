# -*- coding:utf-8 -*-
from xlwt import Workbook
import json

file = open('student.txt','rb')
text = file.read().decode('gbk')
js = json.loads(text)
book = Workbook()
sheet = book.add_sheet('student')
rownum = 0
js2 = sorted(js)
for i in js2:
    colnum = 0
    print i
    sheet.write(rownum,colnum,unicode(i))
    for item in js[i]:
        print item
        colnum += 1
        sheet.write(rownum,colnum,unicode(item))
    rownum += 1
book.save('student.xls')

