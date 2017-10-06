with open('whenyouareold.txt') as f:
    words = f.read()

words = words.split()
#过滤符号
mark = ['《','》',',',';','.']
for word in words:
	for letter in word:
		if letter in mark:
			words[words.index(word)] = word.replace(letter,'')                            

#转换为小写
for word in words:
	words[words.index(word)] = word.lower()

count = dict()
for word in words:
	if word not in count:
		count[word] = 1
	else:
		count[word] += 1

with open('result.txt','w') as f:
    for key in count:
        f.write(key + ' : '+ str(count[key]) + '\n')

