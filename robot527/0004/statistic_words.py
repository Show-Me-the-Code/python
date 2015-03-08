#! usr/bin/python3
"""
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

print('Please input a text file name which in the current working directory.')
print('Usage - example.txt')
file_name = input("@> ")

def deal_punctuation(the_string):
    from string import punctuation as punc
    punc_list = list(punc)
    punc_list.remove('-')
    ret_string = the_string
    for each_punc in punc_list:
        ret_string = ret_string.replace(each_punc, ' ')
    ret_string = ret_string.replace(' -', ' ').replace('- ', ' ')
    return ret_string

def stat(the_file):
    try:
        with open(the_file) as textfile:
            word_list = []
            for each_line in textfile:
                temp = deal_punctuation(each_line)
                word_list += temp.split()
            print('This file has ', word_list.__len__(), ' words.')
            word_set_list = sorted(set(word_list))
            for each_word in word_set_list:
                print(each_word + ' : ', word_list.count(each_word))
    except IOError as err:
        print('File error: ' + str(err))

if __name__ == '__main__':
    stat(file_name)
