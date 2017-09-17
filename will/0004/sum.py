# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

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

if __name__ == '__main__':
    with open(path, 'r') as file:
        data = file.read().lower()
        sumofword = count(data)
        print(sumofword)
        file.close()
