import random, string

def rand_str(num, length = 20):
	#生成num个长度为20的激活码
	with open('activation_code.txt','w') as f:
		for i in range(num):
			chars = string.ascii_letters + string.digits
			s = [random.choice(chars) for i in range(length)]
			f.write('{0}\n'.format(''.join(s)))

if __name__ == '__main__':
	rand_str(200)