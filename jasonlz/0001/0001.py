# coding=utf-8
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random, string

def random_key(length=7):
	con = string.digits + string.letters
 	s = [random.choice(con) for i in range(length)]
 	s = ''.join(s)
 	return s

def save(number):
	f = open('random_key.out','wd')
	for i in range(number):
		s = random_key();
		f.write(str(s)+'\n')
	f.close()
if __name__ == '__main__':
	save(200)