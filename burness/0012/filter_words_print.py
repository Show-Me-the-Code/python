#-*- coding: utf-8-*-

# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:Burness Duan
# Date:2014-12-29
# Python 3.3


def filter_word(input_word):
	input_word = input_word.split()
	filter_word_list = []
	with open('./filter_word.txt','r') as f:
		for content in f:
			filter_word_list.append(content.strip('\n'))
	return filter_word_list

if __name__ == '__main__':
	input_words = input('Input some words')
	input_words_list = input_words.split()
	filter_word_list = filter_word(input_words)
	
	words_string=''
	for word in input_words_list:
		if word in filter_word_list:
			word = '*'*len(word)
		words_string += word + ' '
	print(words_string)


