#!/usr/bin/env python

import xlwt
import json


def load_data(filepath):
    f = open(filepath, "r")
    return json.load(f)

def write_data_to_xls(data):
    xls = xlwt.Workbook()
    sheet = xls.add_sheet("number")

    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i, j, data[i][j])

    xls.save('number.xls')


if __name__ == '__main__':
    data = load_data("number.txt")
    write_data_to_xls(data)




