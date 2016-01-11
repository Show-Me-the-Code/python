"""
    有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
    包括空行和注释，但是要分别列出来。
"""

import os
import re

root_dir = os.getcwd() + "//1001"
code_lines = 0
blank_lines = 0
annotation_lines = 0

for root, dirs, files in os.walk(root_dir):
    for i in files:
        print(root_dir + "\\" + i)
        with open(root_dir + "\\" + i, "r", encoding="utf-8") as f:
            line = f.readline()
            while line != "":
                print(line)
                line = f.readline()
