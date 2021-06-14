# 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re


def word_count(file):
    res = {}
    with open(file, 'r') as f:
        content = f.read()
    temp = re.split(r"[^a-zA-Z]", content)
    for word in temp:
        if not word:
            continue
        word = word.lower()
        if word not in res:
            res[word] = 1
        else:
            res[word] += 1
    return res


res = word_count("english.txt")
print(res)
