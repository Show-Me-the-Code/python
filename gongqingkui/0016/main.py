#0016
import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('numbers')
with open('numbers.txt') as f:
    _numbers = eval(f.read())
i=j=0
for num in range(len(_numbers)):
    for n in _numbers[i]:
        ws.write(i,j,n)
        j = j+1
    i = i + 1
    j = 0
wb.save('numbers.xls')
