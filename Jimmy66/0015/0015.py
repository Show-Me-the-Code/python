#!/bin/env python
# -*- coding: utf-8 -*- 

#导入模块
import simplejson as json  
import xlwt

#从文件(JSON形式)中读取数据返回字典
def read_file(filename):
    with open(filename,'r') as fp:
        content = fp.read()
    d = json.JSONDecoder().decode(content)
    return d  

#生成对应的xls文件
def gen_xls(d,filename):
    fp = xlwt.Workbook()
    table = fp.add_sheet('city',cell_overwrite_ok=True)
    #这次一次循环就可以了
    for n in range(len(d)):
        table.write(n,0,n+1)
        table.write(n,1,d[str(n+1)])
    fp.save('city.xls')
    print '写入完毕'

#主函数
def main():
    filename = 'city.txt'
    xls_name = 'city.xls'
    d = read_file(filename)
    gen_xls(d,xls_name)

if __name__ == '__main__':
    main()
