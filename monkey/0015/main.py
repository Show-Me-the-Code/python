# -*- coding:utf-8 -*-

'''
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，如下图所示：

@Author monkey
@Date   2017-8-31
'''
import json
import xlwt

def getCity():

    with open('city.txt', 'r', encoding='UTF-8') as file:
        text = ''
        for line in file:
            text = text + line

        city_json = json.loads(text, encoding = 'UTF-8')
        print(city_json)

        writeInXLS(city_json)


def writeInXLS(dict):
    fileName = 'city.xls'

    # 创建 文件
    file = xlwt.Workbook()
    # 创建 表
    sheet = file.add_sheet('city', cell_overwrite_ok=True)

    row = 0
    col = 0

    for k, v in sorted(dict.items(), key=lambda d:d[0]):
        sheet.write(row, col, k)
        col += 1
        sheet.write(row, col, v)

        row += 1
        col = 0

    file.save(fileName)

if __name__ == '__main__':
    getCity()
