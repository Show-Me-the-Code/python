# -*- coding: utf-8 -*-
import os

CODE_PATH = os.path.join(os.path.dirname(__file__), '..')

code_files = []
code_line_count = 0
code_blank_line_count = 0
code_comment_line_count = 0


def walk(rootDir):
    global code_files
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            walk(path)
        else:
            if os.path.splitext(lists)[1].upper() == '.PY':
                code_files.append(path)

walk(CODE_PATH)
for code_file in code_files:
    file = open(code_file)
    for line in file:
        code_line_count += 1
        if line == '\n':
            code_blank_line_count += 1
        if line.replace(' ', '').replace('\t', '')[0] == '#':
            code_comment_line_count += 1
print '文件数量：', len(code_files)
print '代码行数：', code_line_count
print '空行行数：', code_blank_line_count
print '注释行数:', code_comment_line_count
