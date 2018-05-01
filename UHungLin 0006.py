#你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
# 假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os
from collections import Counter

# 文件路径
path = 'E:/python/python小程序/0006/'
filesouces = os.listdir(path)

# 过滤词
stop_words = ['a', 'an', 'the', 'is', 'was', 'and', '1']

def get_most_important_words(diaryfilesouce):

    for filesouce in diaryfilesouce:
        if filesouce.endswith(".txt"):
            with open(filesouce) as f:

                files = f.read().split( )
                # 移除需要过滤的词
                files = filter(remove_stop_words, files)
                # 打印
                print(filesouce, Counter(files).most_common()[0][0])

# 过滤函数
def remove_stop_words(n):
    if n not in stop_words:
        return True
    else:
        return False


if __name__ == "__main__":
    get_most_important_words(filesouces)
