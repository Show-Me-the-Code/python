'''
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
# encoding: utf-8
import collections
import os.path
def judgeit(words):
    for i in range(6):
        if len(words[i]) > 2 and words[i] != 'the' and words[i] != 'her' and words[i] !=  'his' and words[i] != 'and' and words[i] != 'she':
            return  words[i]
    return words[7]

def mainKeywords(dirPath):
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == '.txt':
            print('the keywords of' + i + ' is:' )
            with open(i, 'r') as fp:
                str1 = fp.read().split(' ')
            b = collections.Counter(str1)
            keywords = sorted(b, key=lambda x: b[x],reverse = True)
            print(judgeit(keywords))

mainKeywords('D:\PyCharm 2017.1.3\projects')