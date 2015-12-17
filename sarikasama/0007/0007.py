#!/usr/bin/env python3
#count lines of code in directory 'test'

import os

def count_lines(f):
    #get the count of lines in the code
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
    os.chdir('test')
    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            with open(file,'r') as f:
                res[f.name]=count_lines(f)
    return res

if __name__=="__main__":
    res = main()
    for i in res:
        print(i+"\ntotal:"+str(res[i][0])+"\nnote:"+str(res[i][1])+"\nempty_line:"+str(res[i][2]))
        print("\n")
