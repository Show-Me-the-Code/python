'''
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os.path
import re
def mainKeywords(dirPath):
    blank, comments, codelines, totalines, count, temp = 0, 0, 0, 0, 0, 0
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == '.py':
            print(i)
            with open(i, 'r', encoding='utf-8') as fp:
                while True:
                    line = fp.readline()
                    totalines += 1
                    if not line:
                        break
                    elif line.strip().startswith('#'):
                        comments += 1
                    elif line.strip().startswith("'''") or line.strip().startswith('"""'):
                        comments += 1
                        if line.count('"""') == 1 or line.count("'''") == 1:
                            while True:
                                line = fp.readline()
                                totalines += 1
                                comments += 1
                                if ("'''" in line) or ('"""' in line):
                                    break
                    elif line.strip():
                        codelines += 1
                    else:
                        blank += 1
                print('the nuber of totalines is : ' + str(totalines-1))
                print('the nuber of comments is : ' + str(comments))
                print('the nuber of codelines is : ' + str(codelines))
                print('the nuber of blanklines is : ' + str(blank))
                blank, comments, codelines, totalines = 0, 0, 0, 0

mainKeywords('D:\PyCharm 2017.1.3\projects')