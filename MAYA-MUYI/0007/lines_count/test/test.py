import os
import re

re_obj = re.compile('[(//)(/*)(*)(*/)]')

def count_codeline(filename):

    cur_alllines = 0
    cur_codelines = 0
    cur_spacelines = 0
    cur_commentslines = 0
    f = open(filename)
    for line in f:
        cur_alllines += 1
        if line.strip() == '':
            cur_spacelines += 1
            continue
        if re_obj.match(line.strip()):
            cur_commentslines += 1
    cur_codelines = cur_alllines - cur_spacelines - cur_commentslines
    print('%-15s : all_lines(%s)\t code_lines(%s)\t space_lines(%s)\t comments_lines(%s)' % (filename, cur_alllines, cur_codelines, cur_spacelines, cur_commentslines))
    f.close()

if __name__ == '__main__':
    count_codeline('tests.c')
