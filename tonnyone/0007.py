#!/usr/bin/env python
#coding=utf-8

'''有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。'''
__author__ = 'tonnytwo'

import os
import sys

def scanCode(path,linenum=0,codenum=0,emptynum=0):

    print path
    uipath=''
    if isinstance(path, str):
         uipath = unicode(path, "utf8")
         uipath = unicode(path, "utf8")
    elif isinstance(path,unicode):
         uipath = path
    else:
        return None

    if(os.path.isdir(uipath)):
        print "123"
        files = os.listdir(uipath)
        for f in files:
            if(os.path.isdir(uipath+os.sep+f)):
               tupl2 =  scanCode(uipath+os.sep+f,linenum,codenum,emptynum)
               linenum = linenum +tupl2[0]
               codenum = codenum +tupl2[1]
               emptynum = emptynum+tupl2[2]
            else:
                if f.endswith(".py"):
                    tupl1 = getCode(uipath+os.sep+f,linenum,codenum,emptynum)
                    linenum = linenum+tupl1[0]
                    codenum = codenum+tupl1[1]
                    emptynum = emptynum+tupl1[2]
                else:
                    continue
        return linenum,codenum,emptynum
    else:
        return linenum,codenum,emptynum

def getCode(path,linenum=0,codenum=0,emptynum=0):

    sign=[u'/',u'#',u"\'",u"\"",'/','#','/','\'','\"']
    f = open(path,"r")
    for line in f:
         linenum = linenum+1
         if len(line.strip())>0:
             if line.strip()[0] in sign:
                codenum = codenum+1
         else:
             emptynum = emptynum+1

    return linenum,codenum,emptynum

print("你好是不是我说的")
print(sys.getdefaultencoding())
print scanCode(r"E:\eversec\A_document\python\mit\笔记");