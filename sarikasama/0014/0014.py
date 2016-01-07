#!/usr/bin/env python3
#from json to xlsx

import xlsxwriter, json

def json2xls():
    wb = xlsxwriter.Workbook('student.xls')
    ws = wb.add_worksheet("student")

    with open('./student') as f:
        data = json.load(f)
        for i in range(len(data)):
            ws.write(i, 0, i+1)
            json_data = data[str(i+1)]
            for j in range(len(json_data)):
                ws.write(i, j+1, json_data[j])
    wb.close()

if __name__=='__main__':
    json2xls()
