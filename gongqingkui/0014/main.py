#0014
#encoding=utf-8
import json
import xlwt

f = file('student.txt')
data = json.load(f,encoding='gb2312')
#print(json.dumps(data))

wb = xlwt.Workbook()
ws = wb.add_sheet('student')

i=j=0
for item in data:
    ws.write(i,j,item)
    for item2 in data[item]:
        j = j + 1
        ws.write(i,j,item2)    
    i = i+1
    j = 0
wb.save('student.xls')
