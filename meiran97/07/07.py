# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# 学习了os.walk()

import os

root_path = '../'
py_list = []
for root, dirs, files in os.walk(root_path):  # 注意walk的使用方法
    for file in files:
        if file[-3:] == '.py':
            py_list.append(os.path.join(root, file))  # 注意获得完整路径的方法
print(py_list)

row = 0
empty_line = 0
note_line = 0
for py in py_list:
    with open(py) as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                empty_line += 1
            elif line[0] == '#':
                note_line += 1
        row += len(lines)
print('共有%s行代码，包括空行%s行，注释%s行' % (row, empty_line, note_line))
