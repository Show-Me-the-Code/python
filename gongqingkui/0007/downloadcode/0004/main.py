#0004 riji
filename='01.txt'
wordarrays=[]
worddict={}
#xucis=['a','an','The','by','the','in','on','from','above','behind','is','and','but','before','oh','well','hi','of']
with open(filename) as f:
    l = f.readline()
    while l:
        wordarrays.append(l.split())
        l = f.readline()

for wordarray in wordarrays:
    for word in wordarray:
        word = word.lower()
        if word in worddict:
            worddict[word] = worddict.get(word) + 1
        elif word not in worddict:
            worddict[word] = 1
            

sortedwordlist = sorted(worddict.items(),lambda x,y:cmp(x[1],y[1]),reverse=True)
print(sortedwordlist)
'''for xuci in xucis:
    if xuci in worddict:
        del worddict[xuci]
sortedwordlist = sorted(worddict.items(),lambda x,y:cmp(x[1],y[1]),reverse=True)
print(sortedwordlist)
'''
