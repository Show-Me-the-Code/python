cnt = 0
dic = {}
with open('test.txt','r') as f:
    data = f.read().split(' ')

for word in data:
    word = word.lower()
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

for item in sorted(dic.items(),key=lambda x: x[1],reverse=True):
    print(item)