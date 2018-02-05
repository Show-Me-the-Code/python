#0020
#encoding=utf-8
import xlrd
import chardet
import string

def timeParse(timestr):
    ind = timestr.find('\xb7\xd6')
    #print(ind)
    if ind is not -1:
        #print(ind)
        _time = int(timestr[:ind])*60+timeParse(timestr[ind+2:])
    else:
        _time = eval(timestr[:-2])
    return _time

data = xlrd.open_workbook('mobile0632.xls',encoding_override='utf-8')
table = data.sheet_by_name('201801')
total = 0
for row in range(table.nrows):
    total = total + timeParse(table.cell(row,4).value.encode('gb2312'))
    #s.append(table.cell(row,4).value.encode('gb2312'))
print("total seconds:%d"%total)
