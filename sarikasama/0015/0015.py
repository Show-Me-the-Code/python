#!/usr/bin/env python3
#from json to xlsx

import xlsxwriter, json

def json2xls():
    wb = xlsxwriter.Workbook('city.xls')
    ws = wb.add_worksheet("city")

    with open('./city') as f:
        data = json.load(f)
        for i in range(len(data)):
            ws.write(i, 0, i+1)
            ws.write(i, 1, data[str(i+1)])
    wb.close()

if __name__=='__main__':
    json2xls()
