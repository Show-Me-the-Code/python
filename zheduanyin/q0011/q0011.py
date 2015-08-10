# 过滤关键词, 若出现, 则输出Freedom, 否则输出Human Rights
import re
import sys


if __name__ == '__main__':
    data = input('输入需要检索的语句:\n')
    with open('filtered_words.txt') as fp:
        for line in fp.readlines():
            sensitive = re.search(line.strip(), data)
            if sensitive:
                print('Freedom')
                sys.exit()
        print('Human Rights')
