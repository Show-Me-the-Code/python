#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0020
* by ahwz001
* 2017/9/23
* Thanks for this project. I learned a lot here.
"""

import xlrd


def count_the_dail_time(filename):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    row_nums = sheet.nrows
    col_nums = sheet.ncols
    total_time = 0
    for i in range(1,row_nums):
        total_time += int(sheet.cell_value(i,3))
    print total_time
    return total_time


if __name__ == "__main__":
    total_len = count_the_dail_time("0020_SRC.xls")
    print "本月通话时长为: %d 秒" % total_len
