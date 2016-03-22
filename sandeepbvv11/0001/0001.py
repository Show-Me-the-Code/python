import uuid
import random
f=open('IDs.txt','w')
for i in range(0,200):
    x=str(uuid.uuid4().fields[-1])[:10]
    f.write(x+"\n")
f.close()


