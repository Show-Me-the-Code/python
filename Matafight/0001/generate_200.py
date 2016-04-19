#_*_ encoding: utf-8 _*_
import uuid

class generate:
    def __init__(self):
        self.num=0;
        self.listid=[];
    def generate_uuid(self,num):
        for i in range(int(num)):
            self.listid.append(uuid.uuid1());

    def get_uuid(self):
        return self.listid;

if __name__=="__main__":
    gencode=generate();
    gencode.generate_uuid(200);
    keys=gencode.get_uuid();
    filekeys=file("gencodes.txt",'w');
    for key in keys:
        filekeys.write(str(key)+'\n');
    filekeys.close();
        
