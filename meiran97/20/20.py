'''
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方
，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
'''

import pandas as pd

def sum_time(filepath):
    df = pd.read_excel(filepath, skiprows=5)
    df['通话时长'] = df['通话时长'].astype('object')
    df['通话时长'] = pd.to_timedelta(df['通话时长'])
    print('done')
    print('本月共通话了%s' % df['通话时长'].sum())
    return df['通话时长'].sum()

if __name__ == '__main__':
    sum_time('18701969772_通话详单.xls')