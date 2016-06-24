# -*- coding:utf-8 -*-
from xlwt import Workbook
import json

file = open('city.txt','rb')
text = file.read().decode('gbk')
js = json.loads(text)
book = Workbook()
sheet = book.add_sheet('city')
rownum = 0
js2 = sorted(js)
for i in js2:
    colnum = 0
    sheet.write(rownum,colnum,unicode(i))
    sheet.write(rownum,colnum+1,unicode(js[i]))
    rownum += 1
book.save('city.xls')