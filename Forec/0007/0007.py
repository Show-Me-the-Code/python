# coding = utf-8
# Can detect .py / .c / .cpp
__author__ = 'Forec'
import os
import re

def get_line( file_path ):
    file_dir = os.listdir(file_path)
    code ,exp ,space ,alls = ( 0, 0 ,0 , 0)
    cFlag = True
    exp_re = re.compile(r'[\"\'].*?[\"\']')
    for x in file_dir:
        if os.path.isfile(x) and (
            os.path.splitext(x)[1] == '.py'
            or os.path.splitext(x)[1] == '.c'
            or os.path.splitext(x)[1] == '.cpp'
            ):
            try:
                f = open( x, 'r' )
            except:
                print('Cannot open file %s' % x)
            for line in f.readlines():
                alls += 1
                if line.strip() == '' and cFlag:
                    space += 1
                    continue
                find_exp = exp_re.findall(line)
                for strs in find_exp:
                    line = line.replace(strs,'')
                if os.path.splitext(x)[1] == '.py':
                    if '#' in line:
                        exp += 1
                    else :
                        code += 1
                elif os.path.splitext(x)[1] == '.c' or os.path.splitext(x)[1] == '.cpp':
                    if r'*/' in line:
                        cFlag = True
                        exp += 1
                    elif r'/*' in line:
                        cFlag = False
                        exp += 1
                    elif not cFlag:
                        exp += 1
                    elif r'//' in line:
                        exp += 1
                    else:
                        code += 1
            cFlag = True 
            try:
                f.close()
            except:
                pass
                
    print( '''All Lines total : %d
Codes total : %d
Spaces total: %d
Explanation : %d'''
% ( alls, code, space, exp ))

get_line('.')
