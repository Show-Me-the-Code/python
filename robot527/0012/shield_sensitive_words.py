#! /usr/bin/python
# -*- coding: utf-8 -*-
# shield_sensitive_words.py
# author: robot527
# created at 2016-4-26

'''
���д��ı��ļ� filtered_words.txt�����������Ϊÿһ��һ�����дʡ�
����
����Ա
����Ա
�쵼
ţ��
ţ��
����
����
love
sex
jiangge

���û��������д���ʱ�������Ǻ� * �滻��
���統�û����롸�����Ǹ��ó��С������ɡ�**�Ǹ��ó��С���
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
