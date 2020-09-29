import json 
import xlwt
from xlwt import Workbook
wb = Workbook()
fptr = open("./city.txt","r")
test_string = fptr.read()
fptr.close()

sheet1 = wb.add_sheet('Sheet 1') 

res = json.loads(test_string)
i = 0
for item in res:
    
    sheet1.write(i, 0, item)
    sheet1.write(i, 1, res[item])
    i+=1
    
wb.save('city.xls')
print(res)
