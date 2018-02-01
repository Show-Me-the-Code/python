#0015
#encoding=utf-8
import json
import xlwt

f = file('city.txt')
data = json.load(f,encoding='gb2312')

wb = xlwt.Workbook()
ws = wb.add_sheet('city')

i=j=0
for item in data:
    ws.write(i,j,item)
    ws.write(i,1,data[item])    
    i = i+1
wb.save('city.xls')