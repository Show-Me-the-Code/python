#! /usr/bin/python
# -*- coding: utf-8 -*-
# word_filter.py
# author: robot527
# created at 2016-4-22

'''
敏感词文本文件 filtered_words.txt，里面的内容为每一行一个敏感词。
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''

def get_words(words_file):
    '''Get words from words_file'''
    words = []
    text = open(words_file)
    for each_line in text:
        words.append(each_line.strip().decode('gb18030'))
    #for w in words:
    #    print w, type(w)
    text.close()
    return words


def str_to_unicode(str1):
    '''Convert str1 to unicode'''
    if isinstance(str1, unicode):
        return str1
    try:
        string_uni = str1.decode("utf-8")
        return string_uni
    except UnicodeDecodeError as err:
        print err


if __name__ == '__main__':
    sensitive_words = get_words("filtered_words.txt")
    running = True
    while running:
        print 'Please input a word, or press q for exit.'
        try:
            para = raw_input("-> ")
        except EOFError:
            print "If you want to quit, press Q key.\n"
            continue
        #uw = str_to_unicode(para)
        #print uw, type(uw)
        if str_to_unicode(para) in sensitive_words:
            print "Freedom\n"
        elif para is 'q':
            para = raw_input("Do you really want to exit ([y]/n)?")
            if para is not 'n':
                running = False
        else:
            print "Human Rights\n"
