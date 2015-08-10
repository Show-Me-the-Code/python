# 统计单词出现次数
import re

from collections import Counter
from pprint import pprint


def count_words(text, verbose=False):
    prog = re.compile(r'\w+')
    words = prog.findall(text)
    c = Counter()
    for word in words:
        c[word.lower()] += 1
    if verbose:
        pprint(c)
    return c

if __name__ == '__main__':
    test_data = '''
    he is a good boy, but she is a good girl.
    '''
    wc = count_words(test_data)
