import json, xlwt

with open('numbers.txt','r')as f:
    data = f.read().decode('gbk')
data = json.loads(data)

book = xlwt.Workbook(encoding = 'utf-8')
sheet = book.add_sheet('numbers')
for i in range(len(data)):
    for j in range(len(data[i])):
        sheet.write(i,j,data[i][j])
book.save('numbers.xls')
        
