#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

__author__='TonyZhu'

# import os

# print(os.getcwd()+'/words.txt')
def wordStatistics(path):
	wordDict = {}
	with open(path,'r') as file:
		for line in file:
			wordListPerLine = line.split(' ')
			for word in wordListPerLine:
				if wordDict.has_key(word):
					wordCount = wordDict.get(word)
					wordCount+=1
					wordDict[word] = wordCount
				else:
					wordDict[word] = 0
	return wordDict

if __name__ == '__main__':
	import os
	wordDict = wordStatistics(os.getcwd()+'/word.txt')
	for k,v in wordDict.items():
		print('key is %s,value is %s'%(k,v))
