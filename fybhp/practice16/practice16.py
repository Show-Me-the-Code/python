# -*- coding:utf-8 -*-
from xlwt import Workbook
import json

file = open('numbers.txt','rb')
text = file.read()
js = json.loads(text)
book = Workbook()
sheet = book.add_sheet('numbers')
rownum = 0
colnum = 0
for i in range(len(js)):
    for j in range(len(js[i])):
        sheet.write(i,j,str(js[i][j]))
    #rownum += 1
book.save('numbers.xls')