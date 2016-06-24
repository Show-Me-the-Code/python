# -*- coding:utf-8 -*-
import os

#用字典结构表示，更为清晰。
map = {}
map['blank'] = 0
map['annotation'] = 0
map['all'] = 0
dir = r'E://somegit/pracpro/'
file_list = os.walk(dir)

def parsefile(filedir):
    #可以此控制计算的文件类型，如加上'.sql'等，都很容易。
    if filedir[-3:] == '.py':
        h = open(filedir,'r')
        allLines = h.readlines()
        for line in allLines:
            line = line.strip()
            if line == '':
                map['blank'] += 1
            elif line[0] == '#':
                map['annotation'] += 1
        map['all'] += len(allLines)

#这几行很重要。
for root, dirs, files in file_list:
    for name in files:
        #特别是这一行。
        filedir = root+'/'+name
        parsefile(filedir)

print map