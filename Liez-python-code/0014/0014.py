import re
import xlwt

def read2xls(x):
    datatable = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    newsheet = datatable.add_sheet('student', cell_overwrite_ok = True)
    num = 0
    with open(x, 'r') as f:
        text = f.read()
        info = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)]')
        for x in info.findall(text):
            for i in range(len(x)):
                newsheet.write(num, i, x[i])
            num += 1

        datatable.save('liez.xls')

read2xls('student.txt')
