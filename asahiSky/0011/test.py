import os

fileName = 'filtered_words.txt'
nameList = open(fileName,'rt')
nameList = nameList.readlines()

print(nameList)
while True:
	s = input('What do you want to say:')
	if (s+'\n') in nameList:
		print('Freedom')
		continue
	if (s=='exit'):
		break
	else:
		print('Human Rights')

