import os
import re

#定义规则抓取文件中的python注释
re_obj_py = re.compile('[(#)]')
#定义规则抓取文件中的C语言注释
re_obj_c = re.compile('[(//)(/*)(*)(*/)]')


#判断是否为python文件
def is_py_file(filename):
    if os.path.splitext(filename)[1] == '.py':
        return True
    else:
        return False

#判断是否为c文件
def is_c_file(filename):
    if os.path.splitext(filename)[1] in ['.c', '.cc', '.h']:
        return True
    else:
        return False

#定义几个全局变量用于计算所有文件总和(全部行数、代码行数、空行数、注释行数)
all_lines, code_lines, space_lines, comments_lines = 0, 0, 0, 0

#判断是否为文件夹，不是则输出提示
def count_codelines(dirpath):
    if not os.path.isdir(dirpath):
        print('input dir: %s is not legal!' % dirpath)
        return
    # 定义几个全局变量用于计算每个文件行数(全部行数、代码行数、空行数、注释行数)
    global all_lines, code_lines, space_lines, comments_lines
    #列出当前文件夹下的文件(包含目录)
    all_files = os.listdir(dirpath)
    for file in all_files:
        #将文件(目录)名与路径拼接
        file_name = os.path.join(dirpath, file)
        if os.path.isdir(file_name):
            count_codelines(file_name)
        else:
            temp_all_lines, temp_code_lines, temp_space_lines, temp_comments_lines = 0, 0, 0, 0
            f = open(file_name)
            for line in f:
                temp_all_lines += 1
                if line.strip() == '':
                    temp_space_lines += 1
                    continue
                if is_py_file(file_name) and re_obj_py.match(line.strip()):
                    temp_comments_lines += 1
                if is_c_file(file_name) and re_obj_c.match(line.strip()):
                    temp_comments_lines += 1
            temp_code_lines = temp_all_lines - temp_space_lines - temp_comments_lines
            print('%-15s : all_lines(%s)\t code_lines(%s)\t space_lines(%s)\t comments_lines(%s)'
                  % (file, temp_all_lines, temp_code_lines, temp_space_lines, temp_comments_lines))

            all_lines += temp_all_lines
            code_lines += temp_code_lines
            space_lines += temp_space_lines
            comments_lines += temp_comments_lines



if __name__ == '__main__':
    count_codelines('test')
    print('\n**** TOTAL COUNT ****\nall_lines = %s\ncode_lines = %s\nspace_lines = %s\ncomments_lines = %s' % (all_lines, code_lines, space_lines, comments_lines))


