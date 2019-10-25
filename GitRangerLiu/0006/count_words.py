import os
from os.path import join
import re


def count_words(root):
    wdic = {}
    for root, dirs, files in os.walk(root):
        for name in files:            
            filename = join(root, name)

            f = open(filename, 'rb')
            for line in f:
                line = line.lower().strip()
                words = re.findall('[a-zA-Z0-9]+', line)
                for word  in words:
                    if word in wdic:
                        wdic[word] += 1
                    else:
                        wdic[word] = 1
            f.close()
    wdic = sorted(wdic.items(), key = lambda x: x[1], reverse = True)
    print wdic

if __name__ == '__main__':
    root = 'test'
    count_words(root)
