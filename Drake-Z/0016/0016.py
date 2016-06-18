#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
    [1, 82, 65535], 
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中。'''

__author__ = 'Drake-Z'

import json
from openpyxl import Workbook

def txt_to_xlsx(filename):
    file = open(filename, 'r', encoding = 'UTF-8')
    file_cintent = json.load(file, encoding = 'UTF-8')
    print(file_cintent)
    workbook = Workbook()
    worksheet = workbook.worksheets[0]
    for i in range(1, len(file_cintent)+1):
        for m in range(1, len(file_cintent[i-1])+1):
            worksheet.cell(row = i, column = m).value = file_cintent[i-1][m-1]
    workbook.save(filename = 'numbers.xls')

if __name__ == '__main__':
    txt_to_xlsx('numbers.txt')