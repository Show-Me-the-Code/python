import os
import re
from collections import Counter

def get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

def counter_more_words(li):
    words_dict = Counter(li)
    return [i[0] for i in words_dict.most_common()[:10]]

for diaryfile in get_filepaths('diaries'):
    with open(diaryfile) as f:
        word_li = re.findall("\w+", f.read())
        print " ".join(counter_more_words(word_li))

