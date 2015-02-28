# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-08
# Python 3.4

"""

第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

"""

import os
import sys
import re


def important_word(target_file):
    file_object = open(target_file, 'r')
    file_content = file_object.read()

    # Split the string
    p = re.compile(r'[\W\d]*')
    word_list = p.split(file_content)

    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sort = sorted(word_dict.items(), key=lambda e: e[1], reverse=True)

    print("The most word in '%s' is '%s', it appears %s times" % (target_file, sort[0][0], sort[0][1]))
    print("The second most word in '%s' is '%s', it appears %s times" % (target_file, sort[1][0], sort[1][1]))
    file_object.close()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter. Try to execute 'python 0006.py $dir_path'")
    else:
        for dir_path in sys.argv[1:]:
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                important_word(file_path)