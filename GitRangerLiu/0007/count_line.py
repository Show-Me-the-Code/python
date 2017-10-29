import os
from os.path import join
import re

comm = '[(#)(//)(/*)(*)]'
prog = re.compile(comm)

def count_line(root):
    codecount = 0
    emptycount = 0
    commcount = 0
    for root, dirs, files in os.walk(root):
        for name in files:
            filename = join(root, name)
            f = open(filename)
            for line in f:
                if line.strip() == '':
                    emptycount += 1
                #python script
                elif prog.match(line.strip()) != None:
                    commcount += 1
                else:
                    codecount += 1
            f.close()

    print 'code lines: ', codecount
    print 'comment lines: ', commcount
    print 'empty lines: ', emptycount
    
if __name__ == '__main__':
    root = 'test'
    count_line(root)
