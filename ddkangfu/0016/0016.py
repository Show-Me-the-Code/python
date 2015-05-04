# coding=utf-8

import json
import os

import xlwt

"""
0016: 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

    [
        [1, 82, 65535], 
        [20, 90, 13],
        [26, 809, 1024]
    ]

请将上述内容写到 numbers.xls 文件中，如下图所示：

![numbers.xls](http://i.imgur.com/iuz0Pbv.png)
"""


def load_json_file(file_name):
    f = file(file_name)
    json_data = json.load(f)
    return json_data


def save_as_xls(file_name, data):
    excel = xlwt.Workbook()

    file_names = os.path.splitext(os.path.basename(file_name))
    table = excel.add_sheet(file_names[0])

    row = 0

    for item in data:
        table.write(row, 0, item[0])
        table.write(row, 1, item[1])
        table.write(row, 2, item[2])
        row += 1

    excel.save(file_name)


if __name__ == '__main__':
    data = load_json_file("numbers.txt")

    if data:
        save_as_xls('numbers.xls', data)
