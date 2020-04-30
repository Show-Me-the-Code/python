# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# 学习了re.findall()

import os
import re
import collections

# 取得所有文件的路径装入列表
diaries_path = './diaries/'
full_path_list = []
for diary in os.listdir(diaries_path):
    full_path_list.append(os.path.join(diaries_path, diary))
# print(full_path_list)

# 定义count函数，DAY4内容
def find_key_word(file_path):
    with open(file_path, 'r') as fh:
        text = fh.read()
        # text.type = string，下面处理text
        word_list = re.findall(r'[a-zA-Z0-9]+', text.lower())
        for word in word_list:
            if word in ['the', 'i', 'is', 'are', 'you', 'to', 'and', 'it', 'a', 'of', 'this', 'in', 't', 'that', 'be'] :
                word_list.remove(word)
        key_word = collections.Counter(word_list).most_common(1)
        # print(key_word)
        print('在%s文件中，%s为关键字，共出现%s次' % (file_path.split('/')[-1], str(key_word[0][0]), str(key_word[0][1])))

if __name__ == '__main__':
    for i in full_path_list:
        find_key_word(i)
