import json, xlwt

with open('city.txt','r')as f:
    data = f.read().decode('gbk')
data = json.loads(data)

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('city')

for i in range(len(data)):
    sheet.write(i,0,i)
    sheet.write(i,1,data[str(i+1)])
book.save('city.xls')
    
