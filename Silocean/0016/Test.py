__author__ = 'Tracy'
import xlwt

with open('numbers.txt') as f:
    content = f.read()
    lists = eval(content)

file = xlwt.Workbook()
table = file.add_sheet('Test',cell_overwrite_ok=True)

for row in range(len(lists)):
    for col in range(len(lists[row])):
        table.write(row, col, lists[row][col])

file.save('result.xls')