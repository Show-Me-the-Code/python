'''#-*-coding: utf-8-*-
import uuid
class codeGenerate:
    def __init__(self):
        self.num = 0
        self.list =[]
        
    def generate(self,num):
        for i in range(num):
            self.list.append(uuid.uuid1())
                  
    def returnList(self):
        return self.list
        
            
test = codeGenerate()
test.generate(200)
keys = test.returnList()

with open('D:/python workSpace/showmethecode/0001/keys.txt','w') as f:
    f.writelines("%s\n"%item for item in keys)

print(len(keys))
'''

import uuid

class generateKeys:
    def __init__(self):
        self.list = []
        self.id_count = 0
        
    def gengrateId(self,id_count):
        for i in range(id_count):
            self.list.append(uuid.uuid1())
            
    def returnList(self):
        return self.list
        
        
test = generateKeys()
test.gengrateId(200)
keys = test.returnList()

with open('D:/python workSpace/showmethecode/0001/keys1.txt','w') as f:
    f.writelines("%s\n" % a for a in keys)
    
print(len(keys))





















