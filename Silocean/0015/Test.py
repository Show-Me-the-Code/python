__author__ = 'Tracy'
import xlwt

with open('city.txt') as f:
    content = f.read()
    dic = eval(content)

file = xlwt.Workbook()
table = file.add_sheet("Test", cell_overwrite_ok=True)

for k, v in dic.items():
    table.write(int(k)-1, 0, k)
    table.write(int(k)-1, 1, str(v).decode('gbk'))

file.save('result.xls')