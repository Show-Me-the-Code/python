# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数
# 学习了Counter和sorted
import collections
import string


def word_count(file):
    with open(file, 'r') as fh:
        word_list = []
        for line in fh:
            word_list += line.lower().replace(',', '').replace('.', '').split()
    b = collections.Counter(word_list)  # 注意这里Counter
    b = sorted(b.items(), key=lambda x: x[1])  # 注意这里sorted和lambda
    with open('result.txt', 'w') as fh2:
        for i in b:
            fh2.write(i[0] + ':' + str(i[1]) + '\n')
    print(b)


if __name__ == '__main__':
    word_count('LICENSE1.txt')
