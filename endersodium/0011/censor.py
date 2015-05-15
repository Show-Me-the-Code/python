# coding:utf-8
# Python Requriement:3(For Chinese Characters read purpose only)
# Made by EnderSodium ender@enderself.co
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

class filtered(object):
	# Read from txt file.
	def _init_(self):
		global filtered_words
		filtered_temp = open('filtered_words.txt','r')
		temp = filtered_temp.read()
		filtered_words = temp.split('\n')

	def check(self,word):
		free = False
		for i in filtered_words:
			if word == i:
				print('Freedom')
				free = True
				break
		if free != True:
			print('Human Rights')

def main():
	# Assign Objects and initialize
	filtered_words_obj = filtered()
	filtered_words_obj._init_()
	# Read from user
	word = input('Please put in your word.')
	filtered_words_obj.check(word)

if __name__ == '__main__':
	main()