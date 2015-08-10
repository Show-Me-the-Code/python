# 过滤关键词，把敏感词替换为*
import re


if __name__ == '__main__':
    data = input('输入需要检索的语句:\n')
    with open('filtered_words.txt') as fp:
        for line in fp.readlines():
            data = re.sub(line.strip(), '*' * len(line.strip()), data)
        print(data)
