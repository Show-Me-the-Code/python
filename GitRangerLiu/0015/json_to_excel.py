# -*- coding: utf-8 -*-
import json
import xlwt

testfile = 'city.txt'
savename = 'city.xls'
sheetname = 'big city'

def json_to_excel():
    info = get_json(testfile)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetname)

    print info
    row_total = len(info)
    col_total = 1
    #The keys of dict is special, so we just use 1, 2, 3
    for r in range(row_total):
        sheet.write(r, 0, r + 1)

    for r in range(row_total):
        for c in range(col_total):
            #Get values by the key
            val = info[str(r + 1)]
            sheet.write(r, c + 1, val)
    workbook.save(savename)

#Convert json format file to python object  
def get_json(testfile):
    with open(testfile, 'r') as f:
        #The codec should be the same as the file encoding.
        text = f.read().decode('GB2312')
        return json.loads(text)

if __name__ == '__main__':
    json_to_excel()
