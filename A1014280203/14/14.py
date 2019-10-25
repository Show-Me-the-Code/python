import xlwt

with open('student.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    _student = eval(data)
    student = list()
    for i in range(1, 4):
        info = _student[str(i)]
        student.append(i)
        student.extend(info)
    row = len(_student)/len(student)


def horz_left(x, y, data):
    algnt = xlwt.Alignment()
    algnt.horz = xlwt.Alignment.HORZ_LEFT
    style = xlwt.XFStyle()
    style.alignment = algnt
    table.write(x, y, data, style)

file = xlwt.Workbook()
table = file.add_sheet('student')
for i in range(len(student)):
    if not i % 5:
        horz_left(i//5, i % 5, student[i])
    else:
        table.write(i//5, i % 5, student[i])

file.save('student.xls')
