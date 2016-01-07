# coding = utf-8
__author__ = 'Forec'
import xlwt
import re

book = xlwt.Workbook(encoding = 'utf-8', style_compression=0)
sheet = book.add_sheet('student',cell_overwrite_ok = True)
line = 0
info = re.compile(r'\"(\d+)\":\[\"(.*?)\",(\d+),(\d+),(\d+)\]')
with open('student.txt',"r") as f:
    data = f.read()
    data=data.decode('gbk').encode('utf-8')
for x in info.findall(data):
    for i in range(len(x)):
        sheet.write(line,i,x[i])
    line+=1
book.save('student.xls')
