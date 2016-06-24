#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。'''

__author__ = 'Drake-Z'

import os
import re
import xlrd

def jishu(file):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    re_timesec = re.compile(r'([\d]+)秒')
    re_timemin = re.compile(r'([\d]+)分')
    row_nums = table.nrows
    numbers = 0
    for i in range(0, row_nums):
        a = re_timesec.findall(table.cell(i, 3).value)
        b = re_timemin.findall(table.cell(i, 3).value)
        if len(a)==0 : pass
        else:
            numbers += int(a[0])
        if len(b)==0 : pass
        else:
            numbers += int(b[0])*60

    print('您本月通话时长总时：%s 分 %s 秒' % (numbers//60, numbers%60))

file = '语音通信.xls'
jishu(file)