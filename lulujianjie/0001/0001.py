import uuid

uuids = []
for i in range(200):#0-199
	uuids.append(uuid.uuid1())#append把value当作一个整体插入list
i = 0;	
for i in range(200):
        print uuids[i]
