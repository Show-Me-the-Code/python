# coding=utf-8
__author__ = 'PyBeaner'
import os
import fnmatch

total_lines = 0
code_lines = 0
empty_lines = 0
comment_lines = 0


def count_line(line):
    line = line.lstrip()
    global comment_lines, empty_lines, total_lines, code_lines

    total_lines += 1
    if line.startswith("#"):
        comment_lines += 1
    elif not line:
        empty_lines += 1
    else:
        code_lines += 1


def scan_dir(directory, suffix="*.py"):
    directory = os.path.abspath(directory)
    print("Scanning files in %s ..." % directory)
    for cur_dir, dirs, files in os.walk(directory):
        for file in files:
            if not fnmatch.fnmatch(file, suffix):
                continue
            file_path = os.path.join(cur_dir, file)
            with open(file_path, errors="replace") as f:
                for line in f:
                    count_line(line)


if __name__ == '__main__':
    scan_dir(r"../..")
    print("Total lines:%d" % total_lines)
    print("Code lines:%d" % code_lines)
    print("Empty lines:%d" % empty_lines)
    print("Comment lines:%d" % comment_lines)
