#!/usr/bin/env python

import xlwt
import json


def load_data(filepath):
    f = open(filepath, "r")
    return json.load(f)

def write_data_to_xls(data):
    xls = xlwt.Workbook()
    sheet = xls.add_sheet("city")

    print data
    for i in range(len(data)):
        sheet.write(i, 0, i+1)
        json_data = data[str(i+1)]
        sheet.write(i, 1, json_data)

    xls.save('city.xls')


if __name__ == '__main__':
    data = load_data("city.txt")
    write_data_to_xls(data)




