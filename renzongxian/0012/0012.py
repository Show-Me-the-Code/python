# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-22
# Python 3.4

"""

第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

"""


def filter_words(words):
    # Read filtered words from file named 'filtered_words.txt'
    file_object = open('filtered_words.txt', 'r')
    filtered_words = []
    for line in file_object:
        filtered_words.append(line.strip('\n'))
    file_object.close()

    # Check if the input words include the filtered words and replace the filtered with '*'
    for filtered_word in filtered_words:
        if filtered_word in words:
            words = words.replace(filtered_word, '*'*len(filtered_word))

    print(words)

if __name__ == '__main__':
    while True:
        input_words = input('Input some words:')
        filter_words(input_words)

