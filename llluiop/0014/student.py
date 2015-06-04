#!/usr/bin/env python

import xlwt
import json


def load_data(filepath):
    f = open(filepath, "r")
    return json.load(f)

def write_data_to_xls(data):
    xls = xlwt.Workbook()
    sheet = xls.add_sheet("student")


    for i in range(len(data)):
        sheet.write(i, 0, i+1)
        json_data = data[str(i+1)]
        for j in range(len(json_data)):
            sheet.write(i, j+1, json_data[j])

    xls.save('student.xls')


if __name__ == '__main__':
    data = load_data("student.txt")
    write_data_to_xls(data)




