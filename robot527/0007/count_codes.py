#! usr/bin/python3
"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
"""

class PyfileInfo:

    def __init__(self, file):
        self.file_name = file
        self.total_line_num = 0
        self.blank_line_num = 0
        self.comment_line_num = 0
        
    def count_lines(self):
        if self.file_name[-3:] != '.py':
            print(self.file_name + ' is not a .py file!')
            return
        try:
            with open(self.file_name) as code:
                for each_line in code:
                    self.total_line_num += 1
                    temp = each_line.strip()
                    if temp == '':
                        self.blank_line_num += 1
                    elif temp[0] == '#':
                        self.comment_line_num += 1
                    
        except IOError as err:
            print('File error: ' + str(err))

import os
target_path = '.'
file_list = [f for f in os.listdir(target_path)
             if os.path.isfile(os.path.join(target_path, f))]
#print(file_list, len(file_list))

pyfile_list = [os.path.join(target_path, f) for f in file_list
               if f[-3:] == '.py']

print(pyfile_list[0])

pyf1 = PyfileInfo(pyfile_list[0])
pyf1.count_lines()
#pyf2 = PyfileInfo('test.c')
#pyf2.count_lines()

print('==' * 18)
print('Total line number is:', pyf1.total_line_num)
print('Blank line number is:', pyf1.blank_line_num)
print('Comment line number is:', pyf1.comment_line_num)
