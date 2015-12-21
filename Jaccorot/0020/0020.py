#!/usr/bin/python
# coding=utf-8

"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，
点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日
通话详单.xls 文件。写代码，对每月通话时间做个统计。
"""

import xlrd

def count_the_dail_time(filename):
    excel = xlrd.open_workbook(filename)
    sheet = excel.sheet_by_index(0)
    row_nums = sheet.nrows
    col_nums = sheet.ncols
    total_time = 0
    for i in range(1,row_nums):
        total_time += int(sheet.cell_value(i, 3))
    return total_time


if __name__ == "__main__":
    total_len = count_the_dail_time("src.xls")
    print "本月通话时长为" + total_len + "秒"
