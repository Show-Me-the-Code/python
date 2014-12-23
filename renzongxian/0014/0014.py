# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-22
# Python 3.4

"""

第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中。

"""

import xlwt3
import json


# 该部分参考了agmcs的代码，https://github.com/Show-Me-the-Code/python/blob/master/agmcs/0014/0014.py
def write_txt_to_xls(txt_file):
    # Read form the txt file
    txt_object = open(txt_file, 'r')
    file_content = json.load(txt_object)

    # Write to the xls file
    xls_object = xlwt3.Workbook()
    sheet = xls_object.add_sheet('student')
    for i in range(len(file_content)):
        sheet.write(i, 0, i+1)
        data = file_content[str(i+1)]
        for j in range(len(data)):
            sheet.write(i, j+1, data[j])
    xls_object.save('student.xls')


if __name__ == '__main__':
    write_txt_to_xls('student.txt')

