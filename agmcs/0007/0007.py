import os, re 

path = '\..'
blank = 0
comment = 0
total = 0

def getline(path):
    global blank
    global comment
    global total
    with open(path,'r')as f:
        data = f.readlines()
    for x in data:
        if x == '\n':
            blank += 1
        if x.find('#')!= -1:
            if re.search("\'.*?#.*?\'",x) or re.search("\".*?#.*?\"",x):
                pass
            else:
                comment += 1
        total += 1

def getfile(path):
    abspath = os.path.abspath(path)
    dirlist = os.listdir(abspath)
    for x in dirlist:
        curpath = os.path.join(abspath,x)
        if os.path.isfile(curpath):
            if os.path.splitext(curpath)[1] == '.py':
                getline(curpath)
        else:
            getfile(curpath)

getfile('..')

print "total:%d, comment:%d, blank:%d"%(total,comment,blank)
