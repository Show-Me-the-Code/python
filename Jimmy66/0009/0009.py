#!/bin/env python
# -*- coding: utf-8 -*- 

#也不清楚这里说的链接是什么定义，是指a标签还是所有href的链接，这里取后者

#导入模块
import re
import urllib2

#读取文件
def file_read(filename):
    #因为用之前文件方法打开html不行，貌似涉及到编码问题，所以想了个抖机灵的方法，编码坑还是要填啊，在XML里面也要用到
    Req = urllib2.Request("file:./Yixiaohan show-me-the-code.html")  
    r = urllib2.urlopen(Req)
    html = r.read()
    return html

#查找链接，返回列表
def link_find(html):
    match = re.findall(r'href="(http[s]?:[^"]+)"',html)   #加括号可以直接截取...偶然一试才知道，findall和python真强大，爱死
    return match

#主函数，显示链接列表
def main():
    html = file_read('Yixiaohan show-me-the-code.html')
    link = link_find(html)
    for  string in link:
        print string

if __name__ == '__main__':
    main()