# -*-coding:utf-8-*-
import string
class senseWord():
    def __init__(self):
        self.list=[]
        self.word=[]
        inputfile=file('filtered_word.txt','r')
        for lines in inputfile.readlines():
            self.list.append(lines.decode('utf-8').encode('gbk'))#I've set the file coding type as utf-8
        inputfile.close()
        self.list=map(string.strip,self.list);
       
    def checkWord(self,word):
        flag=False
        for words in self.list:
            if words in word:
                self.word.append(words)
                flag= True
        return flag

    def getWord(self):

        return self.word

if __name__=='__main__':
    myCheck=senseWord()
    while True:
        ipstr=str(raw_input())
        if ipstr:
           if(myCheck.checkWord(ipstr)):
               senseList=myCheck.getWord()
               for items in senseList:
                   length=len(items.decode('gbk'))
                   torep='*';
                   for i in range(1,length):
                       torep+='*'
                   ipstr=ipstr.replace(items,torep)
               print ipstr
           else:
               print ipstr
        else:
            break



