import xlwt

with open('city.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    _city = eval(data)
    city = list()
    for i in range(1, 4):
        info = _city[str(i)]
        city.append(i)
        city.append(info)
    row = len(city)//len(_city)


def horz_left(x, y, data):
    algnt = xlwt.Alignment()
    algnt.horz = xlwt.Alignment.HORZ_LEFT
    style = xlwt.XFStyle()
    style.alignment = algnt
    table.write(x, y, data, style)

file = xlwt.Workbook()
table = file.add_sheet('city')
for i in range(len(city)):
    if not i % row:
        horz_left(i//row, i % row, city[i])
    else:
        table.write(i // row, i % row, city[i])
file.save('city.xls')