import uuid
import random
f=open('IDs.txt','w')
st= 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*'
for i in range(0,200):
    x=str(uuid.uuid4().fields[-1])[:10]+st
    y=''
    for j in range(0,10):
         y+=random.choice(x)
    print (y+"\n")
    f.write(y+"\n")
f.close()


