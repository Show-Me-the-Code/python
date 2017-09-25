# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import re
path = './a.txt'

def count(data):
    words = re.compile('[a-zA-Z0-9]+')
    di = {}
    for i in words.findall(data):
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1
    return di

def important_word(worddict):
    maxvalue = max(worddict.values())
    for key in worddict:
        if worddict[key] == maxvalue:
            print(key)
    return

if __name__ == '__main__':
    with open(path, 'r') as file:
        data = file.read().lower()
        sumofword = count(data)
        important_word(sumofword)
        file.close()
