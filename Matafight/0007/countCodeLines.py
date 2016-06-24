#_*_ encoding: utf-8 _*_
import os
import re
#http://www.cnblogs.com/zhoujie/archive/2013/04/10/python7.html
#http://cuiqingcai.com/977.html
class countLines:
        def __init__(self):
            self.comment=0;
            self.codes=0;
            self.blank=0;
            self.fileList=[];#存的是各个文件相关的list
        def openDir(self,dirname):
            curdir=os.getcwd();
            curdir=curdir+str(dirname);
            print curdir
            dirlist=os.listdir(curdir);
            checkpy=re.compile(r"\.py$");
            for item in dirlist:
                if checkpy.search(item):
                    item="\\"+item;
                    self.count(curdir+item);

        def count(self,filename):
            self.comment=0;
            self.codes=0;
            self.blank=0;
            f=file(filename,'r');
            patcomment=re.compile(r"^\s*#");#
            patblank=re.compile(r"^\s+$");#空白字符
            for line in f.readlines():
                if patblank.search(line):
                    self.blank+=1;
                elif patcomment.search(line):
                    self.comment+=1;
                else:
                    self.codes+=1;
            self.fileList.append([filename,self.codes,self.comment,self.blank]);

            f.close();

        def getResult(self):
            return self.fileList;

if __name__=="__main__":
    countInstance=countLines();
    countInstance.openDir(r"\testDir");
    relist=countInstance.getResult();
    for item in relist:
        print item[0];
        print "code num:"+str(item[1]);
        print "comment num:"+str(item[2]);
        print "blank num:"+str(item[3]);
        print "\n"










