#!/bin/env python
# -*- coding: utf-8 -*- 

#导入模块
import simplejson as json  
import xlwt

#从文件(JSON形式)中读取数据返回字典
def read_file(filename):
    with open(r'C:\Python27\oneday_one\student.txt','r') as fp:
        content = fp.read().decode('gbk').encode('utf-8')
        #print type(content)
    #simplejson这个模块还没细看，怎么解码还是需要了解下
    d = json.JSONDecoder().decode(content)
    #d=json.loads(content)
    return d  

#生成对应的xls文件
def gen_xls(d,filename):
    fp = xlwt.Workbook()
    table = fp.add_sheet('student',cell_overwrite_ok=True)
    #试了下，与很多要转utf-8（ASCII码）存文件的情况不同，xls不接受ASCII码形式的存储，直接用字典里面的Unicode就行了，简直好评，不用在特意decode或者encode了
    #想写得更加自动化一些，好复用.本身不太想用两层循环的，不过也不知道有没有更便捷的存储方式（比如整行自动匹配导入，算法是背后优化封装好的，就用了万能的这种方法）
    for n in range(len(d)):
        table.write(n,0,n+1)
        m = 0
        for record in d[str(n+1)]:
            table.write(n,m+1,record)
            m += 1
    fp.save('student.xls')
    print u'写入完毕'

#主函数，嘛，最后还是用“丑陋的二重循环”实现了，但是其实也没什么，还是要看场景和优化，毕竟这也不是做查找或者排序，在日常使用中也不用太担心性能问题
def main():
    filename = 'student.txt'
    xls_name = 'student.xls'
    d = read_file(filename)
    gen_xls(d,xls_name)

if __name__ == '__main__':
    main()
