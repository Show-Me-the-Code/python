import uuid,pickle

class gene_keys():
    def __init__(self,num):
        self.num = num;
        self.list = [];

    def gene_list(self):
        for i in range(self.num):
            key=uuid.uuid1();
            self.list.append(key)

    def return_list(self):
        return self.list;

g=gene_keys(200);
g.gene_list();
keys_list=g.return_list();
#print keys_list

with open('keys.txt','wb') as f:
    for key in keys_list:
        f.write(str(key).replace('-','')+'\n')
            
