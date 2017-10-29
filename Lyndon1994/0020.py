# -*- coding: utf-8 -*-
"""
第 0020 题：
登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，
然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。
写代码，对每月通话时间做个统计。
"""
import time

import re
import xlrd


def str2sec(str):
    print(str)
    sec = 0
    time_re = re.compile(r'(\d+)(\D+)')
    time_list = time_re.findall(str)
    for time_item in time_list:
        if time_item[1] == '秒':
            sec += int(time_item[0])
        elif time_item[1] == '分':
            sec += int(time_item[0]) * 60
        elif time_item[1] == '小时':
            sec += int(time_item[0]) * 3600
    print(sec)
    return sec


def sec2str(sec):
    h = sec // 3600
    m = sec % 3600 // 60
    s = sec % 60
    return '%s小时%s分%s秒' % (h, m, s)


all_time = 0  # 使用总时间（秒）
start_time = time.mktime(time.strptime('2017-03-01', '%Y-%m-%d'))
end_time = time.mktime(time.strptime('2017-04-01', '%Y-%m-%d'))
data = xlrd.open_workbook('source/0020/2017年03月语音通信.xls')
table = data.sheets()[0]
nrows = table.nrows

for i in range(nrows):
    if i == 0:
        continue
    this_time = time.mktime(time.strptime(table.row_values(i)[2], '%Y-%m-%d %H:%M:%S'))
    if this_time >= start_time and this_time < end_time:
        all_time += str2sec(table.row_values(i)[3])

print(sec2str(all_time))
