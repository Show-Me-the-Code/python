'''
It can caculate the words in the text file
'''

import re
def calculate_words(path):
	f = open(path,'r')
	lines = f.readlines()
	count = 0
	for line in lines:
		count+=len(re.split('[,.! ?:]',line))#use the re module to split the txt file 
	return count-len(lines)#the txt file will inlcude the '\n' and '' so sub it

words = calculate_words("C:/Users/razzl/Desktop/1.txt")#in python the '/' can be the path separator in all system
print words
