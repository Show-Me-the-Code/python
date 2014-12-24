# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-23
# Python 3.4

"""

第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中.

"""

import xlwt3
import json


def write_txt_to_xls(txt_file):
    # Read form the txt file
    txt_object = open(txt_file, 'r')
    file_content = json.load(txt_object)

    # Write to the xls file
    xls_object = xlwt3.Workbook()
    sheet = xls_object.add_sheet('numbers')
    for i in range(len(file_content)):
        data = file_content[i]
        for j in range(len(data)):
            sheet.write(i, j, data[j])
    xls_object.save('numbers.xls')


if __name__ == '__main__':
    write_txt_to_xls('numbers.txt')

