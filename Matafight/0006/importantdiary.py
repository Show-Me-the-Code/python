#_*_ encoding: utf-8 _*_
import re

class countWord:
    def __init__(self):
        self.dic={};
        self.word="";


    def count(self,filename):
        self.dic={};
        fopen=file(filename,'r');
        for lines in fopen.readlines():
            words=re.findall(r"\w+",lines);
            for items in words:
                    if items in self.dic.keys():
                        self.dic[items]+=1;
                    else:
                        self.dic[items]=1;
        
        #对字典value值排序
        dict= sorted(self.dic.iteritems(), key=lambda d:d[1], reverse = True);
        self.word=dict[0][0];

    def getWord(self):
        return self.word;


if __name__=="__main__":
    diarycount=countWord();
    order=1;
    importantlist=[];
    for order in range(1,4):
        fname="diary"+str(order)+".txt";
        diarycount.count(fname);
        importantlist.append(diarycount.getWord());
        order+=1; 
    for item in importantlist:
        print str(item)+"\t";
       
   
