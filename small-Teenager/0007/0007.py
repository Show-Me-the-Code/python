# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os


def count_lines(f):
    # get the count of lines in the code
    total = note = empty_row = 0
    line = f.readline()
    while line != '':
        if line[0] == '#':
            note += 1
            total += 1
        elif line == '\n':
            empty_row += 1
            total += 1
        else:
            total += 1
        line = f.readline()
    return total, note, empty_row


def main():
    res = {}
    os.chdir('../0006')
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.py'):
                with open(file, 'r') as f:
                    res[f.name] = count_lines(f)
    return res


res = main()
# file total note empty_line
print(res)
