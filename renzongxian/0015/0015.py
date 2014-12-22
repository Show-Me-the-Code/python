# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-22
# Python 3.4

"""

第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中.

"""

import xlwt3
import json


def write_txt_to_xls(txt_file):
    # Read form the txt file
    txt_object = open(txt_file, 'r')
    file_content = json.load(txt_object)

    # Write to the xls file
    xls_object = xlwt3.Workbook()
    sheet = xls_object.add_sheet('city')
    for i in range(len(file_content)):
        sheet.write(i, 0, i+1)
        data = file_content[str(i+1)]
        sheet.write(i, 1, data)
    xls_object.save('city.xls')


if __name__ == '__main__':
    write_txt_to_xls('city.txt')

