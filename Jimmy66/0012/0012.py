#!/bin/env python
# -*- coding: utf-8 -*- 

#之前没写注释是因为是在Linux下做的，切不出想要的输入法（压根就没倒腾），我要Wine个Bing输入法

#导入模块
import re

#从文件读取信息，以列表形式返回
def read_file(filename):
    l = []
    with open(filename,'r') as fp:
        for line in fp.readlines():
            l.append(line.strip())
    return l

#生成对应的正则匹配规则
def gen_pattern(l):
    #看到好多用join方法的，因为我最初接触的是+，所以比较习惯，外加感觉很爽。如果join比较好的话，我慢慢改吧
    pattern = ''
    for string in l:
        pattern += string + '|'
    #复习了下切片，我刚刚还想试试直接减可不可以，那样python就太酷了，虽然已经非常酷了
    return pattern[:-1]

#输入检测后输出
def input_replace(pattern):
    sentence = raw_input('Please enter a sentence:')
    #直接替换了，懒得先检测,然后判断分支了，没有就不替换
    print re.sub(pattern,'**',sentence)   #如何在字符串变量前面加r并且被识别，这个问题值得考虑下(已解决)写成形如 pattern = r'abc' 即可  

#主函数
def main():
    filename = 'filtered_words.txt'
    l = read_file(filename)
    pattern = gen_pattern(l)
    input_replace(pattern)

if __name__ == '__main__':
    main()


