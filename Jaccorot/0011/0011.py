#!/usr/bin/python
# coding=utf-8

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights。
"""


def trans_to_words():
    type_in = raw_input(">")
    judge_flag = False
    with open('filtered_words.txt') as f:
        text = f.read().decode('utf-8').encode('gbk')

    for i in text.split("\n"):
        if i in type_in:
            judge_flag = True

    if judge_flag:
        print "Freedom"
    else:
        print "Human Rights"


if __name__ == "__main__":
    while True:
        trans_to_words()
