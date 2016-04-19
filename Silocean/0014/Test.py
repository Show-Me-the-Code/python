__author__ = 'Tracy'
import xlwt

with open('Student.txt', 'r') as f:
    content = f.read()

dic = eval(content)

file = xlwt.Workbook()
table = file.add_sheet('Test', cell_overwrite_ok=True)


def deal(key, value):
    table.write(int(key) - 1, 0, key)
    for x in range(len(value)):
        table.write(int(key) - 1, x + 1, str(value[x]).decode('gbk'))

for key, value in dic.items():
    deal(key, value)

file.save('result.xls')
