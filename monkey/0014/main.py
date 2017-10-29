# -*- coding:utf-8 -*-

'''

第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中。

@Author monkey
@Date   2017-8-31
'''
import json
import xlwt

def getStudent():

    with open('student.txt', 'r', encoding = 'UTF-8') as file:
        text = ''
        for line in file:
            text = text + line

        stu_json = json.loads(text, encoding = 'UTF-8')

    print(stu_json)

    writeInXLS(stu_json)


def writeInXLS(dict):
    fileName = 'student.xls'
    # 创建 xls 文件
    file = xlwt.Workbook(encoding = 'utf-8')
    # 创建 表
    sheet = file.add_sheet('student', cell_overwrite_ok=True)

    row = 0
    col = 0

    for k, v in sorted(dict.items(), key=lambda d:d[0]):
        sheet.write(row, col, k)
        for i in v:
            col += 1
            sheet.write(row, col, i)

        row += 1
        col = 0

    file.save(fileName)
    print('写入成功')

if __name__ == '__main__':
    getStudent()