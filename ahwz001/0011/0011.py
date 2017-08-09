#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0011
* by ahwz001
* 2017/8/9
* thanks this project, I learned some very useful Program.
* Please refer to the project folder AK-wang, I learned this code from that.
"""


def filtered_words(f_file):
    filtered_list = []
    with open(f_file) as fn:
        for line in fn:
            t = line.strip()
            filtered_list.append(t)
    return filtered_list


def filtered_or_not(input_word, f_file):
    filtered_words_list = filtered_words(f_file)
    return input_word in (filtered_words_list)


def print_user_input(input_word, f_file):
    if filtered_or_not(input_word,f_file):
        return "Freedom"
    else:
        return "Human Rights"


def main():
    input_word = raw_input("Please input your word>:")
    f_file = "filtered_words.txt"
    print print_user_input(input_word,f_file)


if __name__ == '__main__':
    main()
