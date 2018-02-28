#0011
filteredwords=[]

with open('filtered_words.txt','r')as f:
    #print(f.readlines().encoding('utf8'))
    for l in f.readlines():
        filteredwords.append(l.strip())

#print filteredwords
ins = raw_input("please input:")
if ins in filteredwords:
    print("Freedom")
else:
    print("human rights")
