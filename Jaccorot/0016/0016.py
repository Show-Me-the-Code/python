#!/usr/bin/python
# coding=utf-8

"""
 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
请将上述内容写到 numbers.xls 文件中，如下图所示：
"""

import os
import json
import xlwt

def read_txt(path):
    with open(path, 'r') as f:
        text = f.read().decode('utf-8')
        text_json = json.loads(text)
    return text_json


def save_into_excel(content_dict, excel_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("numbers",  cell_overwrite_ok=True)
    row = 0
    col = 0
    for i in content_dict:
        for k in i:
            ws.write(row, col, k)
            col += 1
        row += 1
        col = 0

    wb.save(excel_name)


if __name__ == "__main__":
    read_content = read_txt(os.path.join(os.path.split(__file__)[0], 'numbers.txt'))
    save_into_excel(read_content, 'numbers.xls')
