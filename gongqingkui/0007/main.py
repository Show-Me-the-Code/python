#0007 count of code,comment,space of dir
import os

def linehead(c):
    if c=='#':
        return 0,1,0
    elif c=='\n':
        return 0,0,1
    else:
        return 1,0,0
    
def count(code,comment,space,c):
    a,b,c = linehead(c)
    return code + a,comment + b,space + c 

if __name__ =='__main__':
    #codepath="../../../downloadcode"
    codepath="./downloadcode"
    tcommentcount,tspacecount,tcodecount = 0,0,0
    g = os.walk(codepath,topdown=True)
    '''root now process
        dirs list of flode (not include sub flode)
        files list of file
    '''
    for root,dirs,files in g:
        for filename in files:
            if os.path.splitext(filename)[1] == '.py':
                commentcount,spacecount,codecount = 0,0,0
                with open(root+"/"+filename) as f:
                    l = f.readline()
                    while l:
                        codecount,commentcount,spacecount = count(codecount,commentcount,spacecount,l[0])
                        l = f.readline()
                    #print ("File:%s%s Code:%dSpace:%dComment:%d"%(root,filename,codecount,spacecount,commentcount))
                    tcommentcount = tcommentcount + commentcount
                    tspacecount = tspacecount + spacecount
                    tcodecount = tcodecount + codecount
print("Total:Code:%d Comment:%d Space:%d"%(tcodecount,tcommentcount,tspacecount))
