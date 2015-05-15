# -*- coding: utf-8 -*-

import os

# Get all files in designated path
def get_files(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path + '/' + fp
        if(os.path.isfile(fppath)):
            files.append(fppath)
        elif(os.path.isdir(fppath)):
            files += get_files(fppath)
    return files

# Count lines and blank lines and note lines in designated files
def count_lines(files):
    line, blank, note = 0, 0, 0
    for filename in files:
        f = open(filename, 'rb')
        for l in f:
            l = l.strip()
            line += 1
            if l == '':
                blank += 1
            elif l[0] == '#' or l[0] == '/':
                note += 1
        f.close()
    return (line, blank, note)

if __name__ == '__main__':
    files = get_files('.')
    print files
    lines = count_lines(files)
    print 'Line(s): %d, black line(s): %d, note line(s): %d' % (lines[0], lines[1], lines[2])
