# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
1.startswith() 
    用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
2.strip()
    用于移除字符串头尾指定的字符（默认为空格）。
'''
import os
path = '.'

def count_line(dir_path):
    if not os.path.isdir(dir_path):
        return
    file_list = os.listdir(dir_path)
    line_num = 0
    null_line = 0
    comment_line = 0
    flag = False
    for file in file_list:
        file_path = os.path.join(dir_path, file)
        if file_path.lower().endswith('py'):
            with open(file_path) as file_handle:
                for line in file_handle.readlines():
                    line_num += 1
                    if line.strip().startswith('\'\'\'') and not flag:
                        comment_line += 1
                        flag = True
                        continue
                    if line.strip().startswith('\'\'\''):
                        comment_line += 1
                        flag = False
                    if line.strip().startswith(r'#') or flag:
                        comment_line += 1
                    if line.strip() == '':
                        null_line += 1
        print("在%s中，共有%d行代码，有%d行空行，有%d行注释" %(file_path, line_num, null_line, comment_line))

if __name__ == '__main__':
    count_line(path)
