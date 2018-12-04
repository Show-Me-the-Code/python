import os
import re

re_obj_py = re.compile('[(#)]')
re_obj_c = re.compile('[(//)(/*)(*)(*/)]')

def is_py_file(filename):
    if os.path.splitext(filename)[1] == '.py':
        return True
    else:
        return False

def is_c_file(filename):
    if os.path.splitext(filename)[1] in ['.c', '.cc', '.h']:
        return True
    else:
        return False

all_lines, code_lines, space_lines, comments_lines = 0, 0, 0, 0

def count_codeline(dirpath):
    if not os.path.isdir(dirpath):
        print('input dir: %s is not legal!' % dirpath)
        return

    global all_lines, code_lines, space_lines, comments_lines

    cur_filelist = os.listdir(dirpath)
    for name in cur_filelist:
        filename = os.path.join(dirpath, name)
        if os.path.isdir(filename):
            count_codeline(filename)
        else:
            cur_alllines, cur_codelines, cur_spacelines, cur_commentslines = 0, 0, 0 ,0
            f = open(filename)
            for line in f:
                cur_alllines += 1
                if line.strip() == '':
                    cur_spacelines += 1
                    continue
                if is_py_file(filename) and re_obj_py.match(line.strip()):
                    cur_commentslines += 1
                if is_c_file(filename) and re_obj_c.match(line.strip()):
                    cur_commentslines += 1
            cur_codelines = cur_alllines - cur_spacelines - cur_commentslines
            print('%-15s : all_lines(%s)\t code_lines(%s)\t space_lines(%s)\t comments_lines(%s)' % (name, cur_alllines, cur_codelines, cur_spacelines, cur_commentslines))

            all_lines += cur_alllines
            code_lines += cur_codelines
            space_lines += cur_spacelines
            comments_lines += cur_commentslines


if __name__ == '__main__':
    count_codeline('mycode')
    # code_lines = all_lines - space_lines - comments_lines
    print('\n**** TOTAL COUNT ****\nall_lines = %s\ncode_lines = %s\nspace_lines = %s\ncomments_lines = %s' % (all_lines, code_lines, space_lines, comments_lines))
