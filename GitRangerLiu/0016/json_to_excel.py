# -*- coding: utf-8 -*-
import json
import xlwt

testfile = 'numbers.txt'
savename = 'numbers.xls'
sheetname = 'number'

def json_to_excel():
    info = get_json(testfile)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetname)

    print info
    row_total = len(info)
    col_total = len(info[0])
    
    for r in range(row_total):
        for c in range(col_total):
            val = info[r][c]
            sheet.write(r, c, val)
    workbook.save(savename)

#Convert json format file to python object  
def get_json(testfile):
    with open(testfile, 'r') as f:
        #The codec should be the same as the file encoding.
        text = f.read().decode('GB2312')
        return json.loads(text)

if __name__ == '__main__':
    json_to_excel()
