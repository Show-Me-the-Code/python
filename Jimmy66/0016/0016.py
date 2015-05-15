#!/bin/env python
# -*- coding: utf-8 -*- 

#导入模块
import simplejson as json  
import xlwt

#从文件(JSON形式)中读取数据返回列表
def read_file(filename):
    with open(filename,'r') as fp:
        content = fp.read()
    l = json.JSONDecoder().decode(content)
    return l 

#生成对应的xls文件
def gen_xls(l,filename):
    fp = xlwt.Workbook()
    table = fp.add_sheet('numbers',cell_overwrite_ok=True)
    #列表的遍历，用index真的好方便，内存循环踩了个坑，要改用row而不是l作为索引对象
    for row in l:
        for col in row:
            table.write(l.index(row),row.index(col),col)  #row表示行，col表示列，后者的英文不一定匹配，我还是再查找下，list.index()可以得到列表中对于元素的索引值
    fp.save(filename)
    print '写入完毕'

#主函数，我猜这次返回的应该是列表吧
def main():
    filename = 'numbers.txt'
    xls_name = 'numbers.xls'
    l = read_file(filename)
    gen_xls(l,xls_name)

if __name__ == '__main__':
    main()
