# -*- coding: utf-8 -*-
'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''

def filter_word():
    f = open('filtered_words.txt', 'rb')
    words = [line.strip() for line in f]
    #Chinese character encoding and decoding, ide encoding, display problem
    #print words
    
    while(True):      
        x = raw_input('请输入文字:(提示： 输入CTRL + C ，退出)\n')
        if x in words:
            print 'Freedom'
        else:
            print 'Human Rights'
    
if __name__ == '__main__':
    filter_word()
