import re

__author__ = 'monkey'

def countWords():
    # 打开文件
    with open('text.txt', 'r') as file:
        data = file.read()

    words = re.compile(r'([a-zA-Z]+)')

    # 统计每个单词出现个个数
    dic = {}
    for i in words.findall(data):
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    # 将字典里面的item保存到list中
    numlist = []
    for k,value in dic.items():
        numlist.append((k, value))

    # 排序
    numlist.sort(key = lambda  t:t[0])

    # 输出结果
    for i in numlist:
        print(i[0], i[1])

if __name__ == '__main__':
    countWords()