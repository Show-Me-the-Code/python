#coding:utf-8
import json
import xlwt

with open('student.txt','r')as f:
    data = f.read().decode('gbk')
data = json.loads(data)

book =xlwt.Workbook(encoding = 'utf-8')
sheet =book.add_sheet('student')

for i in range(len(data)):
    d = data[str(i+1)]
    sheet.write(i,0,i+1)
    for j in range(len(d)):
        sheet.write(i,j+1,d[j])
book.save('student.xls')
