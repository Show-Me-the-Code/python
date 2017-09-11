import xlwt

with open('numbers.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    _numbers = eval(data)
    numbers = list()
    for i in range(3):
        numbers.extend(_numbers[i])
    row = len(numbers)//len(_numbers)

file = xlwt.Workbook()
table = file.add_sheet('numbers')
for i in range(len(numbers)):
    table.write(i // row, i % row, numbers[i])
file.save('numbers.xls')
