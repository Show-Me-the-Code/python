import uuid

i = 1
while (i < 201):
	f = open('code.md', 'ar+')
	s = str(i)+". "+str(uuid.uuid4()) 
	f.write(s+"\n")
	i +=1
