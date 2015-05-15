# -*-coding:utf-8-*-
import string

class senseWord():
    def __init__(self):
        self.list=[]
        inputfile=file('filtered_word.txt','r')
        for lines in inputfile.readlines():
            self.list.append(lines.decode('utf-8').encode('gbk'))#I've set the file coding type as utf-8 
        inputfile.close()
        self.list=map(string.strip,self.list);
        for item in self.list:
            print item
    def checkWord(self,word):
        for words in self.list:
            if words == word:
                return True
        return False

if __name__=='__main__':
    myCheck=senseWord()
    ipstr=raw_input()
    while True:
        ipstr=raw_input()
        if ipstr:
           if(myCheck.checkWord(ipstr)):
               print 'Freedom'
           else:
               print 'humanRight'
        else:
            break


