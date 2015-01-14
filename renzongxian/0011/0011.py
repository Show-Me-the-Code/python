# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-21
# Python 3.4

"""

第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

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

"""


def filter_words(words):
    # Read filtered words from file named 'filtered_words.txt'
    file_object = open('filtered_words.txt', 'r')
    filtered_words = []
    for line in file_object:
        filtered_words.append(line.strip('\n'))
    file_object.close()

    # Check if the input words include the filtered words
    filtered = False
    for filtered_word in filtered_words:
        if filtered_word in words:
            filtered = True
            break

    if filtered is True:
        print('Freedom')
    else:
        print('Human Rights')

if __name__ == '__main__':
    while True:
        input_words = input('Input some words:')
        filter_words(input_words)

