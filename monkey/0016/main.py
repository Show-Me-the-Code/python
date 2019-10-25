# -*- coding:utf-8 -*-

'''
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中，如下图所示：

@Author monkey
@Date   2017-8-31
'''
import json
import xlwt

def getNumber():

    with open('numbers.txt', 'r', encoding='UTF-8') as file:
        text = ''
        for line in file:
            text = text + line

        number_json = json.loads(text, encoding = 'UTF-8')
        print(number_json)

        writeInXLS(number_json)


def writeInXLS(list):
    fileName = 'numbers.xls'

    # 创建 文件
    file = xlwt.Workbook()
    # 创建 表
    sheet = file.add_sheet('numbers', cell_overwrite_ok=True)

    row = 0
    col = 0


    for l in list:
        for i in l:
            sheet.write(row, col, i)
            col += 1

        row += 1
        col = 0

    file.save(fileName)

if __name__ == '__main__':
    getNumber()
