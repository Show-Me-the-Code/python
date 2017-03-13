#-*- coding:utf-8 -*-
import os

codeLines = 0
commentLines = 0
blankLines = 0

def CountLines(countDir,ext,ignore):
    
    global codeLines
    global commentLines
    global blankLines

    for file in os.listdir(countDir):
        if os.path.isdir(os.path.join(countDir,file)) and file != ignore:
            CountLines(os.path.join(countDir,file),ext,ignore)
        else:
            if os.path.splitext(file)[1].strip('.') == ext:
                print(file)
                with open(os.path.join(countDir,file),'r',encoding='utf-8') as f:
                    for line in f:
                        if line.strip().startswith('#'):
                            commentLines = commentLines + 1
                        elif line.strip() == '':
                            blankLines = blankLines + 1
                        else:
                            codeLines = codeLines + 1
    
    


if __name__ == '__main__':
    countDir = input('文件夹路径:')
    ext = input('文件类型:')
    ignore = input('需要忽略的文件夹:')
   
    CountLines(countDir,ext,ignore)
    print('代码行数:%d，注释行数:%d，空行数:%d'%(codeLines,commentLines,blankLines))