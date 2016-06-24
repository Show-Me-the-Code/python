# coding:utf-8
# Python Requirement:3
# Made by EnderSodium ender@enderself.co
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random

# Generate alphabetical stuff
def gene_let(code):
	randomnum = random.randint(65,90)
	temp = chr(randomnum)
	return code + temp

# Generate numerical stuff
def gene_num(code):
	temp = str(random.randint(0,9))
	return code + temp

def generate():
	code = ''
	code = gene_let(code)
	code = gene_num(code)
	code = gene_num(code)
	code = gene_let(code)
	code = gene_num(code)
	code = gene_let(code)
	code = gene_num(code)
	code = gene_num(code)
	code = gene_let(code)
	code = gene_num(code)
	print code

def main():
	for i in range(199):
		generate()

if __name__ == '__main__':
	main()