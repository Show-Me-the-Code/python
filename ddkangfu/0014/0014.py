# coding=utf-8

import json

import xlwt

"""
0014: 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
    {
        "1":["张三",150,120,100],
        "2":["李四",90,99,95],
        "3":["王五",60,66,68]
    }
请将上述内容写到 student.xls 文件中，如下图所示：

![student.xls](http://i.imgur.com/nPDlpme.jpg)
"""


def load_json_file(file_name):
    f = file(file_name)
    json_data = json.load(f)
    return json_data


def save_as_xls(file_name, data):
    excel = xlwt.Workbook()

    table = excel.add_sheet('sheet0')

    row = 0

    for k, v in data.items():
        table.write(row, 0, k)
        table.write(row, 1, v[0])
        table.write(row, 2, v[1])
        table.write(row, 3, v[2])
        table.write(row, 4, v[3])

        row += 1

    excel.save(file_name)


if __name__ == '__main__':
    data = load_json_file("student.txt")

    if data:
        save_as_xls('student.xls', data)
