# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词

import os
import re


def most_important_word(f):
    # get the count of words in the text
    res = {}
    content = f.read()
    tmp = re.split(r"[^a-zA-Z]", content)
    for w in tmp:
        if not w:
            continue
        w = w.lower()
        if w not in res:
            res[w] = 1
        else:
            res[w] += 1
    # get the word of most importance
    res[''] = 0
    max = ''
    for i in res:
        if res[i] > res[max]:
            max = i
    return max


def main():
    res = {}
    os.chdir('txt')
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            with open(file, 'r') as f:
                res[f.name] = most_important_word(f)
    return res


print(main())
