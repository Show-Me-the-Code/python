# -*- coding: utf-8 -*-


#list all the files in your path(完整路径名path\**.py)
import os
def get_files(path):
    files=os.listdir(path)
    files_path=[]
    for fi in files:
        fi_path= path+'\\' + fi
        if os.path.isfile(fi_path):
            if fi.split('.')[-1]=='py':
                files_path.append(fi_path)
        elif(os.path.isdir(fi_path)):
            files_path+=get_files(fi_path)
    return files_path

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
    a=r'c:\python27'
    #files = get_files(r'c:\python27\oneday_one')
    files = get_files(r'F\v6:')
    print len(files),files
    lines = count_lines(files)
    print 'Line(s): %d, black line(s): %d, note line(s): %d' % (lines[0], lines[1], lines[2])
            
