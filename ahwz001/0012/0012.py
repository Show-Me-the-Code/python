#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0012
* by ahwz001
* 2017/8/9
* thanks this project, I learned some very useful Program.
* Please refer to the project folder AK-wang, I learned this code from that.
"""

def filtered_words(f_file):
    """get the filter word list from f_file"""
    filtered_list = []
    with open(f_file) as fn:
        for line in fn:
            t = line.strip()
            filtered_list.append(t)
    return filtered_list


def filtered_or_not(input_word, f_file):
    """get the words need to repalce,return a list of that"""
    filtered_words_list = filtered_words(f_file)
    replace_words = []
    for wd in filtered_words_list:
        if wd in input_word:
            replace_words.append(wd)
    return replace_words


def print_user_input(input_word, f_file):
    """replace the word, if there is someone need to replace."""
    replace_words = filtered_or_not(input_word,f_file)
    # print replace_words
    res = input_word
    if replace_words:
        for i in replace_words:
            res = res.replace(i,"**")
    else:
        pass
    return res


def main():
    # input_word = raw_input("Please input your word>:")
    input_word = "北京欢迎你,牛比,love you!"
    print input_word
    f_file = "filtered_words.txt"
    print print_user_input(input_word,f_file)


if __name__ == '__main__':
    main()
