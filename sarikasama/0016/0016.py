#!/usr/bin/env python3
#from json to xlsx

import xlsxwriter, json

def json2xls():
    wb = xlsxwriter.Workbook('numbers.xls')
    ws = wb.add_worksheet("numbers")

    with open('./numbers') as f:
        data = json.load(f)
        for i in range(len(data)):
            for j in range(len(data[i])):
                ws.write(i, j, data[i][j])
    wb.close()

if __name__=='__main__':
    json2xls()
