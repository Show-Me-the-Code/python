#! /usr/bin/python
# -*- coding: utf-8 -*-
# shield_sensitive_words.py
# author: robot527
# created at 2016-4-26

'''
敏感词文本文件 filtered_words.txt，里面的内容为每一行一个敏感词。
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

当用户输入敏感词语时，则用星号 * 替换，
例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

def get_replace_str(word):
    '''Generate word replace string for word'''
    if word.isalnum():
        return '*' * len(word)
    else:
        return '*' * (len(word) / 3)


def get_words_dict(words_file):
    '''Generate word replace dictionary from words_file'''
    words = {}
    text = open(words_file)
    for each_line in text:
        word = each_line.strip()
        words[word] = get_replace_str(word)
    text.close()
    return words


if __name__ == '__main__':
    sensitive_words = get_words_dict("filtered_words.txt")
    running = True
    while running:
        print 'Please input a sentence, or press q for exit.'
        try:
            para = raw_input("-> ")
        except EOFError:
            print "If you want to quit, press Q key.\n"
            continue
        if para is 'q':
            para = raw_input("Do you really want to exit ([y]/n)?")
            if para is not 'n':
                running = False
        else:
            for each in sensitive_words.keys():
                para = para.replace(each, sensitive_words[each])
            print para, '\n'
