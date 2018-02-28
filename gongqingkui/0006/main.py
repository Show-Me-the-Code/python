#0006
import os

monthlydiary ='./monthly_diary'
wordarrays=[]
worddict={}
xucis=['will','our','if','are','this','there','for','its','be','that','you','we','to','a','an','The','by','the','in','on','from','above','behind','is','and','but','before','oh','well','hi','of']

filelists = os.listdir(monthlydiary)
for fl in filelists:
    filename = os.path.join(monthlydiary,fl)
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
            

    for xuci in xucis:
        if xuci in worddict:
            del worddict[xuci]

    sortedwordlist = sorted(worddict.items(),lambda x,y:cmp(x[1],y[1]),reverse=True)
    print(filename,sortedwordlist[0])
